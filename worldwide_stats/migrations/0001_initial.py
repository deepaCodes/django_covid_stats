# Generated by Django 3.0.7 on 2020-06-23 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('population', models.PositiveIntegerField(verbose_name='population')),
                ('tz', models.CharField(blank=True, max_length=50)),
                ('visits', models.PositiveIntegerField()),
                ('commonwealth', models.NullBooleanField()),
                ('flag', models.FileField(blank=True, upload_to='country/flags/')),
                ('continent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='worldwide_stats.Continent')),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='CovidCasesByCountry',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('country', models.CharField(max_length=200, verbose_name='Country Name')),
                ('flag', models.ImageField(upload_to=None, verbose_name='Country Flag')),
                ('tests', models.IntegerField(verbose_name='Total Tests')),
                ('testsPerOneMillion', models.IntegerField(verbose_name='Test/Million')),
                ('population', models.IntegerField(verbose_name='Population')),
                ('cases', models.IntegerField(verbose_name='Total Cases')),
                ('todayCases', models.IntegerField(verbose_name='Today Cases')),
                ('deaths', models.IntegerField(verbose_name='Total Deaths')),
                ('todayDeaths', models.IntegerField(verbose_name='Todays Deaths')),
                ('critical', models.IntegerField(blank=True, default=0, verbose_name='Critical Cases')),
                ('recovered', models.IntegerField(verbose_name='Total Recovered')),
                ('todayRecovered', models.IntegerField(verbose_name='Today Recovered')),
                ('casesPerOneMillion', models.IntegerField()),
                ('deathsPerOneMillion', models.IntegerField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'CovidCasesByCountry',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='full name')),
                ('friendly', models.BooleanField(default=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='worldwide_stats.Country')),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
    ]
