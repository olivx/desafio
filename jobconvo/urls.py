from django.conf.urls import include, url
from django.contrib import admin

from core.views import home

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home, name='home'),
    url(r'^core/', include('core.urls', namespace='core')),
    url(r'^company/', include('company.urls', namespace='company')),
    url(r'^accounts/', include('jobauth.urls', namespace='accounts')),




]
