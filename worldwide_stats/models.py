from django.db import models
from django.utils.translation import gettext_lazy as _


class Continent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    """
    Represents a geographical Country
    """

    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField(verbose_name=_("population"))
    tz = models.CharField(max_length=50, blank=True)
    visits = models.PositiveIntegerField()
    commonwealth = models.NullBooleanField()
    flag = models.FileField(upload_to="country/flags/", blank=True)

    continent = models.ForeignKey(Continent, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = _("countries")

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=200, verbose_name="full name")
    friendly = models.BooleanField(default=True)

    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "people"

    def __str__(self):
        return self.name


class CovidCasesByCountry(models.Model):
    id = models.IntegerField(verbose_name='Id', primary_key=True)
    country = models.CharField(verbose_name='Country Name', max_length=200)
    flag = models.ImageField(verbose_name='Country Flag', upload_to=None)
    tests = models.IntegerField(verbose_name='Total Tests')
    testsPerOneMillion = models.IntegerField(verbose_name='Test/Million')
    population = models.IntegerField(verbose_name='Population')
    cases = models.IntegerField(verbose_name='Total Cases')
    todayCases = models.IntegerField(verbose_name='Today Cases')
    deaths = models.IntegerField(verbose_name='Total Deaths')
    todayDeaths = models.IntegerField(verbose_name='Todays Deaths')
    critical = models.IntegerField(verbose_name='Critical Cases', blank=True, default=0)
    recovered = models.IntegerField(verbose_name='Total Recovered')
    todayRecovered = models.IntegerField(verbose_name='Today Recovered')
    casesPerOneMillion = models.IntegerField()
    deathsPerOneMillion = models.IntegerField()
    updated = models.DateTimeField()

    class Meta:
        verbose_name_plural = "CovidCasesByCountry"

    def __str__(self):
        return self.country
