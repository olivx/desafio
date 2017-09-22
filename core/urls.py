from django.conf.urls import url
from core import views as core_views

urlpatterns = [

    url(r'list/$', core_views.job_list, name='job_list'),
    url(r'detail/(?P<pk>\d+)/$', core_views.job_detail, name='job_detail'),

    url(r'company/$', core_views.company_list, name='company_list'),
    url(r'company/save/$', core_views.company_save, name='company_save'),
    url(r'company/update/(?P<pk>\d+)/$', core_views.company_update, name='company_update'),
    url(r'company/delete/(?P<pk>\d+)/$', core_views.company_delete, name='company_delete'),


]
