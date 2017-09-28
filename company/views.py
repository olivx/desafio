# -*- coding: utf-8 -*-
from django.db.models import Q
from django.contrib import messages
from cuser.models import CUser as User
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.shortcuts import resolve_url as r, render, get_object_or_404, redirect

# Create your views here.
from core.utils import distance
from company.forms import CompanyForm, JobForm
from jobauth.forms import CandidateForm
from company.models import Company, Job
from company.services import view_service_company_save, \
    view_service_company_delete, view_service_job_save, view_service_job_delete
from core.models import Address
from core.utils import paginator
from jobauth.models import Profile, Candidate


@login_required(login_url='/accounts/login/')
def job_candidate(request, job, user):
    # usuario precisa estar logano no site
    if not request.user.is_authenticated:
        messages.warning(request, 'Vocé deve fazer o login no site para poder se cadastrar as vagas!')
        return redirect(r('company:job_list'))

    # usuario precisa ter um endereço para fazer o cadastro no site.
    if not Address.objects.filter(user=request.user).first():
        messages.warning(request, 'Vocé deve fazer cadastrar o seu endereço antes de se cadastrar!')
        return redirect(r('company:job_list'))

    job = get_object_or_404(Job, pk=job)
    user = get_object_or_404(User, pk=user)
    if request.method == 'POST':
        job.users.add(user)
        job.save()
        message = u'parabens você abaca de se candidatar a vaga de {}!' \
            .format(job.name.upper()) \
            .encode('utf-8')
        messages.success(request, message)

    _list = Job.objects.all()
    jobs = paginator(request=request, object_list=_list, por_page=5)
    context = {
        'job_list': jobs
    }
    return render(request, 'company/job/job_list.html', context)


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
    return view_service_company_delete(request=request, object=obj, Form=CompanyForm, klass=Company,
                                       context_list='company_list',
                                       template_table='company/company_table.html',
                                       message_success=message_delete,
                                       template_name='company/company_modal_delete.html')


def job_detail(request, pk):
    data = {}
    job = get_object_or_404(Job, pk=pk)
    form = JobForm(instance=job, company=job.company)
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
                                 template_table='company/job/job_table_company.html',
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
    return view_service_job_delete(request=request, object=obj, Form=JobForm, klass=Job,
                                   context_list='job_list',
                                   template_table='company/job/job_table_company.html',
                                   message_success=message_delete,
                                   template_name='company/job/job_modal_delete.html')


@login_required(login_url='/accounts/login/')
def job_cadidate_list(request):
    search = request.GET.get('search')
    if search is None:
        jobs = Job.objects.filter(users=User.objects.get(pk=request.user.id))
    else:
        jobs = Job.objects.filter((Q(users=User.objects.get(pk=request.user.id))) &
                                  Q(name__icontains=search))

    return render(request, 'company/job/job_candidated_list.html', {'job_list': jobs})

@login_required(login_url="/accounts/login")
def job_candidate_company(request):
    search = request.GET.get('search')
    if search is None:
        jobs = Job.objects.filter(company__user=request.user)
    else:
        jobs = Job.objects.filter(Q(company__user=request.user) & Q(name__icontains=search))
    return render(request, 'company/job/job_candidated_list_company.html', {'job_list': jobs})

@login_required(login_url="/accounts/login")
def job_candidate_company_profile(request, pk, user, company):
    template = 'company/job/job_candidate_company_profile.html'
    job = Job.objects.get(pk=pk)
    user = User.objects.get(pk=user)
    company = Company.objects.get(pk=company)
    candidate_form = Candidate.objects.get(user=user)
    dis = distance(user.address, company.address)
    _distancia = int(dis['rows'][0]['elements'][0]['distance']['value'])/1000
    if _distancia < job.distancia_max:
        css = " bg-success "
        text_info = "Requisito satisfatório"
    else:
        css = " bg-danger "
        text_info = "Requisito não satisfatório"
    context = {
        'user': user,
        'css': css,
        'text_info': text_info,
        'distance_text': dis['rows'][0]['elements'][0]['distance']['text'],
        'percurso_text': dis['rows'][0]['elements'][0]['duration']['text'],
        'candidate_form': CandidateForm(instance=candidate_form)
    }
    return render(request, template, context)
