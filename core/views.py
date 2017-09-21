from django.shortcuts import render
from core.models import Company
from django.db.models import Q


# Create your views here.

def home(request):
    return render(request, 'core/index.html')


def vagas_list(request):
    search = request.GET.get('search')
    if search is not None:
        _list = Company.objects.filter(Q(vaga__icontains=search))
    else:
        _list = Company.objects.all()
    return render(request, 'core/vagas_list.html', {'vaga_list': _list})
