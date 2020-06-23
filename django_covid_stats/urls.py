"""django_covid_stats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.urls import include
from django.urls import path
from django.views.generic.base import TemplateView
from rest_framework.generics import ListAPIView

from worldwide_stats.views import (
    index,
    MultipleTables,
    PersonListView,
    CovidListView,
)


class HealthCheckView(ListAPIView):
    """
    Checks to see if the site is healthy.
    """

    def get(self, request, *args, **kwargs):
        return HttpResponse('OK')


urlpatterns = [
    path('', index),
    # path('', TemplateView.as_view(template_name='index.html')),
    path('multitable/', MultipleTables.as_view()),
    path('person/', PersonListView.as_view()),
    path('covid/', CovidListView.as_view()),
    path('admin/', admin.site.urls),
    path('ping', HealthCheckView.as_view()),
]

# Only serve static files from Django during development
# Use Google Cloud Storage or an alternative CDN for production
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += staticfiles_urlpatterns() + [path("__debug__/", include(debug_toolbar.urls))]
