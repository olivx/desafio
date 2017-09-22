from django.shortcuts import render, get_object_or_404, redirect , resolve_url as r
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from jobauth.models import Profile
from core.models import Company, Job
from core.forms import JobForm
from django.db.models import Q


# Create your views here.

def home(request):
    return render(request, 'core/index.html')


def job_list(request):
    search = request.GET.get('search')
    if search is not None:
        _list = Job.objects.filter(Q(name__icontains=search) | Q(copany__name__icontains=search))
    else:
        _list = Job.objects.all()
    return render(request, 'core/job_list.html', {'job_list': _list})


def job_detail(request, pk):
    data = {}
    job = get_object_or_404(Job, pk=pk)
    form = JobForm(instance=job)
    data['disable_all'] = True
    data['html_form'] = \
        render_to_string('core/job/job_detail.html', {'form': form}, request=request)
    return JsonResponse(data)


@login_required(login_url='/accounts/login/')
def company_list(request):
    if request.user.profile.kind == Profile.EMPLOYEE:
        return redirect(r('core:job_list'))
    return render(request, 'core/company_list.html')
