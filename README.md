
# Django project setup
mkdir django_covid_stats

cd django_covid_stats

django-admin startproject django_covid_stats .

django-admin startapp worldwide_stats

python manage.py migrate
