from django.conf.urls import url
from core import views as core_views

urlpatterns = [


    url(r'profile_save/(?P<pk>\d+)/$', core_views.profile_save, name='profile_save'),




]
