from random import choice
from datetime import datetime
from django.shortcuts import render
from django.utils.lorem_ipsum import words
from django.views.generic import ListView, TemplateView
from django_tables2 import RequestConfig, MultiTableMixin, SingleTableView
import requests
from .data import COUNTRIES
from .models import Country, Person, CovidCasesByCountry
from .tables import (
    Bootstrap4Table,
    PersonTable,
    ThemedCountryTable, ThemedCovidTable)


def create_fake_data():
    # create some fake data to make sure we need to paginate
    if Country.objects.all().count() < 50:
        for country in COUNTRIES.splitlines():
            name, population = country.split(";")
            Country.objects.create(name=name, visits=0, population=int(population))

    if Person.objects.all().count() < 100:
        countries = list(Country.objects.all()) + [None]
        Person.objects.bulk_create(
            [Person(name=words(3, common=False), country=choice(countries)) for i in range(50)]
        )


def load_covid_data():

    CovidCasesByCountry.objects.all().delete()

    url = "https://corona.lmao.ninja/v2/countries?sort=cases"

    payload = {}
    headers = {
        'Cookie': '__cfduid=d50f9ba4267da0577f6d8df0ef2ec4a871592874495'
    }

    response = requests.get(url, headers=headers, data=payload)
    response.raise_for_status()

    result = response.json()
    country_list = []
    for row in result:
        country_list.append(CovidCasesByCountry(id=row['countryInfo']['_id'], country=row['country'],
                                                tests=row['tests'], testsPerOneMillion=row['testsPerOneMillion'],
                                                cases=row['cases'], todayCases=row['todayCases'], deaths=row['deaths'],
                                                recovered=row['recovered'], population=row['population'],
                                                casesPerOneMillion=row['casesPerOneMillion'],
                                                deathsPerOneMillion=row['deathsPerOneMillion'],
                                                todayRecovered=row['todayRecovered'],
                                                critical=row['critical'],todayDeaths=row['todayDeaths'],
                                                updated=datetime.fromtimestamp(row['updated']/1000),
                                                flag=row['countryInfo']['flag']
                                                ))

    CovidCasesByCountry.objects.bulk_create(country_list)
    print('Covid cases loaded')

create_fake_data()
load_covid_data()

def index(request):
    """Demonstrate the use of the bootstrap4 template"""

    table = Bootstrap4Table(Person.objects.all(), order_by="-name")
    RequestConfig(request, paginate={"per_page": 10}).configure(table)

    return render(request, "bootstrap4_template.html", {"table": table})


class PersonListView(SingleTableView):
    table_class = ThemedCountryTable
    queryset = Country.objects.all()
    template_name = "class_based.html"


class MultipleTables(MultiTableMixin, TemplateView):
    template_name = "multiTable.html"

    table_pagination = {"per_page": 10}

    def get_tables(self):
        qs = Person.objects.all()
        return [
            PersonTable(qs),
        ]


class CovidListView(SingleTableView):
    model = CovidCasesByCountry
    table_class = ThemedCovidTable
    queryset = CovidCasesByCountry.objects.order_by('-cases')
    template_name = "covid_cases.html"
