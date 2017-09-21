from cuser.forms import AuthenticationForm
from django.conf.urls import url
from django.contrib.auth.views import login
from jobauth.views import logout_thanks , signup

urlpatterns = [

    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'signup', signup, name='signup'),
    url(r'logout', logout_thanks, name='logout_tanks'),
    url(r'^login/$', login, {
        'template_name': 'jobauth/login.html',
        'authentication_form': AuthenticationForm,
    }, name='login'),
]
