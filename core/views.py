from django.shortcuts import render, get_object_or_404, redirect, resolve_url as r
from core.services import view_service_save, view_service_delete
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from core.forms import JobForm, CompanyForm
from core.models import Company, Job
from django.http import JsonResponse
from jobauth.models import Profile
from core.utils import paginator
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


@login_required(login_url="/accounts/login")
def job_save(request):
    obj = Job()
    message_save = 'Oportunidade  foi adicionada com sucesso'
    return view_service_save(request=request, object=obj, Form=JobForm, klass=Job,
                             message_type='success',
                             context_list='job_list',
                             message_success=message_save,
                             template_table='core/job/job_table.html',
                             template_name='core/job/job_modal_save.html', )


@login_required(login_url="/accounts/login")
def job_update(request, pk):
    obj = get_object_or_404(Job, pk=pk)
    message_update = 'Oportunidade %s foi alterada com sucesso' % obj.name.upper()
    return view_service_save(request=request, object=obj, Form=JobForm, klass=Job,
                             message_type='warning',
                             context_list='job_list',
                             message_success=message_update,
                             template_table='core/job/job_table.html',
                             template_name='core/job/job_modal_update.html', )


@login_required(login_url="/accounts/login")
def job_delete(request, pk):
    obj = get_object_or_404(Job, pk=pk)
    message_delete = 'Job %s foi deletado com sucesso' % obj.name.upper()
    return view_service_delete(request=request, object=obj, Form=JobForm, klass=Job,
                               context_list='job_list',
                               template_table='core/job/job_table.html',
                               message_success=message_delete,
                               template_name='core/job/job_modal_delete.html')




@login_required(login_url='/accounts/login/')
def company_list(request):
    if request.user.profile.kind == Profile.EMPLOYEE:
        return redirect(r('core:job_list'))
    jobs = paginator(request=request, object_list=Job.objects.all(), por_page=5)
    companies = paginator(request=request, object_list=Company.objects.all(), por_page=5)
    context = {
        'company_list': companies,
        'job_list': jobs
    }
    return render(request, 'core/company_list.html', context)


@login_required(login_url='/accounts/login')
def company_save(request):
    obj = Company()
    return view_service_save(request=request, object=obj, Form=CompanyForm, klass=Company,
                             template_name='core/company/company_modal_save.html', context_list='company_list',
                             template_table='core/company/company_table.html',
                             message_success='Compania foi adcionada com sucesso', )


@login_required(login_url="/accounts/login")
def company_update(request, pk):
    obj = get_object_or_404(Company, pk=pk)
    message_update = 'Compania %s foi alterada com sucesso' % obj.name.upper()
    return view_service_save(request=request, object=obj, Form=CompanyForm, klass=Company,
                             message_type='warning',
                             context_list='company_list',
                             message_success=message_update,
                             template_table='core/company/company_table.html',
                             template_name='core/company/company_modal_update.html')


@login_required(login_url="/accounts/login")
def company_delete(request, pk):
    obj = get_object_or_404(Company, pk=pk)
    message_delete = 'Compania %s foi deletada com sucesso' % obj.name.upper()
    return view_service_delete(request=request, object=obj, Form=CompanyForm, klass=Company,
                               context_list='company_list',
                               template_table='core/company/company_table.html',
                               message_success=message_delete,
                               template_name='core/company/company_modal_delete.html')
