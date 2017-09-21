from cuser.forms import AuthenticationForm
from django.conf.urls import url
from django.contrib.auth.views import login
from jobauth.views import logout_thanks

urlpatterns = [

    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'logout', logout_thanks, name='logout_tanks'),
    url(r'^accounts/login/$', login, {
        'template_name': 'core/login.html',
        'authentication_form': AuthenticationForm,
    }, name='login'),
]
