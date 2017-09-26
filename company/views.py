# -*- coding: utf-8 -*-
from django.db.models import Q
from django.contrib import messages
from cuser.models import CUser as User
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.shortcuts import resolve_url as r, render, get_object_or_404, redirect

# Create your views here.
from company.forms import CompanyForm, JobForm
from company.models import Company, Job
from company.services import view_service_company_save, view_service_delete, view_service_job_save
from core.utils import paginator
from jobauth.models import Profile


@login_required(login_url='/accounts/login/')
def job_candidate(request, job, user):
    job = get_object_or_404(Job, pk=job)
    user = get_object_or_404(User, pk=user)
    if request.method == 'POST':
        job.users.add(user)
        job.save()
        message = u'parabens você abaca de se candidatar a essa vaga!'.encode('utf-8')
        messages.success(request, message)

    return render(request, 'company/job/job_detail.html',
                  {'form': JobForm(instance=job)})


@login_required(login_url='/accounts/login/')
def company_list(request):
    if request.user.profile.kind == Profile.EMPLOYEE:
        return redirect(r('company:job_list'))

    companies = Company.objects.all()
    companies = paginator(request=request, object_list=companies, por_page=5)
    context = {
        'company_list': companies,
    }
    return render(request, 'company/company_list.html', context)


@login_required(login_url='/accounts/login')
def company_save(request):
    obj = Company()
    return view_service_company_save(request=request, object=obj, Form=CompanyForm, klass=Company,
                                     template_name='company/company_modal_save.html',
                                     context_list='company_list',
                                     template_table='company/company_table.html',
                                     message_success='Compania foi adcionada com sucesso', )


@login_required(login_url="/accounts/login")
def company_update(request, pk):
    obj = get_object_or_404(Company, pk=pk)
    message_update = 'Compania %s foi alterada com sucesso' % obj.name.upper()
    return view_service_company_save(request=request, object=obj, Form=CompanyForm, klass=Company,
                                     message_type='warning',
                                     context_list='company_list',
                                     message_success=message_update,
                                     template_table='company/company_table.html',
                                     template_name='company/company_modal_update.html')


@login_required(login_url="/accounts/login")
def company_delete(request, pk):
    obj = get_object_or_404(Company, pk=pk)
    message_delete = 'Compania %s foi deletada com sucesso' % obj.name.upper()
    return view_service_delete(request=request, object=obj, Form=CompanyForm, klass=Company,
                               context_list='company_list',
                               template_table='company/company_table.html',
                               message_success=message_delete,
                               template_name='company/company_modal_delete.html')


def _job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    form = JobForm(instance=job,company=job.company)
    return render(request, 'company/job/job_detail.html', {'form': form, 'company': job.company})


def job_detail(request, pk):
    data = {}
    job = get_object_or_404(Job, pk=pk)
    form = JobForm(instance=job,company=job.company)
    context = {'form': form, 'company': job.company}
    data['disable_all'] = True
    data['html_form'] = render_to_string('company/job/job_detail.html', context, request=request)
    return JsonResponse(data)


def job_detail_list(request, job, userid):
    users = Job.objects.all()
    user_list = paginator(request, users)
    return render(request, 'company/job/job_users_list.html', {'user_list': user_list})


@login_required(login_url="/accounts/login")
def job_list_company(request, pk):
    search = request.GET.get('search')
    company = get_object_or_404(Company, pk=pk)

    if search is not None:
        _list = Job.objects.filter(Q(name__icontains=search) & Q(company=company))
    else:
        _list = Job.objects.filter(company_id=pk)
    jobs = paginator(request=request, object_list=_list, por_page=5)

    context = {
        'company': company,
        'job_list': jobs
    }

    if company.address is None:
        messages.warning(request, 'você precisa cadastrar o endereço da Empresa antes de cadastrar a vaga!')
        return redirect(r('company:company_list'))

    return render(request, 'company/job/job_list_company.html', context)


def job_list(request):
    search = request.GET.get('search')

    if search is not None:
        _list = Job.objects.filter(Q(name__icontains=search) | Q(company__name__icontains=search))
    else:
        _list = Job.objects.all()
    jobs = paginator(request=request, object_list=_list, por_page=5)

    context = {
        'job_list': jobs
    }

    return render(request, 'company/job/job_list.html', context)


@login_required(login_url="/accounts/login")
def job_save(request, company_id):
    obj = Job()
    company = get_object_or_404(Company, pk=company_id)
    message_save = 'Oportunidade  foi adicionada com sucesso'
    return view_service_job_save(request=request, object=obj, company=company, Form=JobForm, klass=Job,
                                 message_type='success',
                                 context_list='job_list',
                                 message_success=message_save,
                                 template_table='company/job/job_table.html',
                                 template_name='company/job/job_modal_save.html', )


@login_required(login_url="/accounts/login")
def job_update(request, pk):
    obj = get_object_or_404(Job, pk=pk)
    message_update = 'Oportunidade %s foi alterada com sucesso' % obj.name.upper()
    return view_service_job_save(request=request, object=obj,
                                 Form=JobForm,
                                 klass=Job,
                                 company=obj.company,
                                 message_type='warning',
                                 context_list='job_list',
                                 message_success=message_update,
                                 template_table='company/job/job_table_company.html',
                                 template_name='company/job/job_modal_update.html', )


@login_required(login_url="/accounts/login")
def job_delete(request, pk):
    obj = get_object_or_404(Job, pk=pk)
    message_delete = 'Job %s foi deletado com sucesso' % obj.name.upper()
    return view_service_delete(request=request, object=obj, Form=JobForm, klass=Job,
                               context_list='job_list',
                               template_table='company/job/job_table.html',
                               message_success=message_delete,
                               template_name='company/job/job_modal_delete.html')
