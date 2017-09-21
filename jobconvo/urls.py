from cuser.forms import AuthenticationForm
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from core.views import home

urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('jobauth.urls', namespace='accounts')),
    url(r'^job/', include('core.urls', namespace='core')),

]
