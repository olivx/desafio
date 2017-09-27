# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect , resolve_url as r
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
# Create your views here.
from jobauth.forms import SignUpForm, CandidateForm
from core.forms import AddressFormPerfil
from jobauth.models import Candidate
from core.models import Address
from core.utils import distance


def logout_thanks(request):
    logout(request)
    return render(request, 'jobauth/logout.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.kind = form.cleaned_data.get('type')
            user.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'jobauth/signup.html', {'form': form})


def address_candidate(request):
    template = 'jobauth/candidate_profile.html'
    candidate = Candidate.objects.filter(user__id=request.user.id).first()
    address = Address.objects.filter(user=request.user).first()
    print address
    candidate_form = CandidateForm(instance=candidate)
    context = {
        'candidate_form': candidate_form,
        'address': address
    }
    return render(request, template, context)


def address_save(request):
    data = {}
    template = 'jobauth/address_save.html'
    address_form = AddressFormPerfil(request.POST or None, user=request.user)
    if request.method == 'POST':
        if address_form.is_valid():
            address_form.save()
            data['is_form_valid'] = True
            data['redirect_url'] = redirect(r('accounts:address_candidate')).url
            messages.info(request, 'não é possivel addcionar um segundo endereço. ')
        else:
            data['is_form_valid'] = False
    context = {'address_form': address_form}
    data['html_form'] = render_to_string(template, context, request=request)
    return JsonResponse(data)


def candidate_save(request, template='jobauth/candidate_profile.html'):
    candidate = Candidate.objects.filter(user__id=request.user.id).first()
    if request.method == 'POST':
        candidate_form = CandidateForm(request.POST, instance=candidate)
        if candidate_form.is_valid():
            cand = candidate_form.save(commit=False)
            cand.user = request.user
            cand.save()
            msg = u'Candidto cadastrado com sucesso'.encode('utf-8')
            messages.success(request, msg)
        else:
            msf_error = u'Verifique os erros a baixo.'.encode('utf-8')

            messages.error(request, msf_error)
            context = {
                'candidate_form': candidate_form,
            }
            return render(request, template, context)
    else:
        candidate_form = CandidateForm(instance=candidate)
    context = {
        'candidate_form': candidate_form,
    }
    return render(request, template, context)


def candidate_delete(request, template='jobauth/candidate_profile.html'):
    candidate = Candidate.objects.filter(user__id=request.user.id).first()
    if request.method == 'POST':
        if candidate is not None:
            candidate.delete()
            msg = u'Informações deletadas com sucesso.'.encode('utf-8')
        else:
            msg = u'Não há informações a serem deletadas.'.encode('utf-8')
        messages.error(request, msg)
    context = {
        'candidate_form': CandidateForm()
    }
    return render(request, template, context)


def profile_address_delete(request, template='jobauth/candidate_profile.html'):
    candidate = Candidate.objects.filter(user__id=request.user.id).first()
    address = Address.objects.filter(user__id=request.user.id).first()
    address_form = AddressFormPerfil(instance=candidate)
    candidate_form = CandidateForm(instance=address)
    if request.method == 'POST':
        if address_form.is_valid():
            address.delete()
            msg = u'Endereco deletado com sucesso'.encode('utf-8')
            messages.error(request, msg)
        else:
            msf_error = u'Formulario com seu endereço não é valido'.encode('utf-8')
            messages.error(request, msf_error)
    context = {
        'address_form': address_form,
        'candidate_form': candidate_form
    }
    return render(request, template, context)


def profile_detail(request, user, template='jobauth/profile_modal.html'):
    data = {}
    candidate = Candidate.objects.filter(user__id=user).first()
    candidate_form = CandidateForm(instance=candidate)
    context = {
        'candidate_form': candidate_form,
    }
    address_candidate = Address.objects.filter(user__id=user).first()
    address_company = Address.objects.filter(company__user=request.user).first()

    data['distancia'] = \
        distance(origin=address_candidate,
                 destination=address_company,
                 api_key=settings.API_TOKEN)

    data['html_form'] = render_to_string(template, context, request=request)
    return JsonResponse(data)
