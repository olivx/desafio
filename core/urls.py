from django.conf.urls import url
from core.views import vagas_list

urlpatterns = [

    url(r'^vagas/list/', vagas_list, name='vagas_list'),

]
