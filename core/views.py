from django.shortcuts import render, get_object_or_404, redirect, resolve_url as r
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from core.forms import JobForm, CompanyForm
from core.models import Company, Job
from django.http import JsonResponse
from django.contrib import messages
from jobauth.models import Profile
from django.db.models import Q
from core.utils import paginator


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
    companies = paginator(request=request, object_list=Company.objects.all(), por_page=5)
    context = {
        'company_list': companies
    }
    return render(request, 'core/company_list.html', context)


@login_required(login_url='/accounts/login')
def company_save(request):
    template_save = 'core/company/company_model_save.html'
    template_table = 'core/company/company_table.html'
    message_success = 'Compania foi adcionada com sucesso'
    message_error = 'Foi encontrado algo errado no processo, ' \
                    'corrija os erros a baixo no formulario e tente novamente'
    data = {}
    form = CompanyForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['is_form_valid'] = True
            companies = paginator(request, Company.objects.all())
            data['html_table'] = \
                render_to_string(template_table, {'company_list': companies}, request=request)

            message = message_success
            messages.error(request, message)
            data['message'] = render_to_string('core/messages.html', {}, request=request)

        else:
            data['is_form_valid'] = False
            message = message_error
            messages.error(request, message)
            data['message'] = render_to_string('core/messages.html', {}, request=request)
            data['html_form'] = \
                render_to_string(template_save, {'form': form}, request=request)
    else:
        data['html_form'] = \
            render_to_string(template_save, {'form': form}, request=request)

    return JsonResponse(data)
