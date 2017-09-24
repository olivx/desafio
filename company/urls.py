from django.conf.urls import url
from company import views as company_views
urlpatterns = [

    url(r'company/$', company_views.company_list, name='company_list'),
    url(r'company/save/$', company_views.company_save, name='company_save'),
    url(r'company/update/(?P<pk>\d+)/$', company_views.company_update, name='company_update'),
    url(r'company/delete/(?P<pk>\d+)/$', company_views.company_delete, name='company_delete'),

    url(r'job/list/$', company_views.job_list, name='job_list'),
    url(r'job/save/$', company_views.job_save, name='job_save'),
    url(r'job/detail/(?P<pk>\d+)/$', company_views.job_detail, name='job_detail'),
    url(r'job/update/(?P<pk>\d+)/$', company_views.job_update, name='job_update'),
    url(r'job/delete/(?P<pk>\d+)/$', company_views.job_delete, name='job_delete'),

]
