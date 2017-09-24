# -*- coding: utf-8 -*-
from cuser.forms import AuthenticationForm
from django.conf.urls import url
from jobauth import views as views_auth

urlpatterns = [


    url(r'profile/$', views_auth.profile, name='profile'),
    url(r'profile/address/update/', views_auth.profile_address_save,
        name='profile_address_save'),
    url(r'profile/candidate/update/', views_auth.profile_candidate_save,
        name='profile_candidate_save'),
    url(r'profile/address/delete/', views_auth.profile_address_delete,
        name='profile_address_delete'),
    url(r'profile/candidate/delete/', views_auth.profile_candidate_delete,
        name='profile_candidate_delete'),

    url(r'signup', views_auth.signup, name='signup'),
    url(r'logout', views_auth.logout_thanks, name='logout_tanks'),
    url(r'^login/$', views_auth.login, {
        'template_name': 'jobauth/login.html',
        'authentication_form': AuthenticationForm,
    }, name='login'),



]
