from django.conf.urls import url
from company import views as company_views
urlpatterns = [

    url(r'company/$', company_views.company_list, name='company_list'),
    url(r'company/save/$', company_views.company_save, name='company_save'),
    url(r'company/update/(?P<pk>\d+)/$', company_views.company_update, name='company_update'),
    url(r'company/delete/(?P<pk>\d+)/$', company_views.company_delete, name='company_delete'),

    url(r'job/list/',company_views.job_list, name='job_list'),
    url(r'job/company/list/(?P<pk>\d+)',
        company_views.job_list_company , name='job_list_company'),

    url(r'job/save/(?P<company_id>\d+)/$', company_views.job_save, name='job_save'),
    url(r'job/detail/(?P<pk>\d+)/$', company_views.job_detail, name='job_detail'),
    url(r'job/update/(?P<pk>\d+)/$', company_views.job_update, name='job_update'),
    url(r'job/delete/(?P<pk>\d+)/$', company_views.job_delete, name='job_delete'),
    url(r'job/candidate/(?P<job>\d+)/(?P<user>\d+)$',
        company_views.job_candidate, name='job_candidate'),

    url(r'job/users/list/(?P<job>\d+)/(?P<userid>\d+)',
        company_views.job_detail_list, name='job_detail_list'),
]
