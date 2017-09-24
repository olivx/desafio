from django.conf.urls import url
from core import views as core_views

urlpatterns = [



    url(r'company/address/delete/(?P<company_id>\d+)/(?P<address_id>\w+)/$',
        core_views.address_delete, name='address_delete'),

    url(r'company/address/update/(?P<company_id>\d+)/(?P<address_id>\w+)/$',
        core_views.address_update, name='address_update'),

    url(r'company/address/save/(?P<company_id>\d+)/$',
        core_views.address_save, name='address_save'),

    url(r'company/address/(?P<company_id>\d+)/$', core_views.address, name='address'),


]
