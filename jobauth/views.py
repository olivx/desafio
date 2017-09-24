# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from core.forms import AddressForm
from core.models import Address
from jobauth.forms import SignUpForm, CandidateForm
from jobauth.models import Candidate


def logout_thanks(request):
    logout(request)
    return render(request, 'jobauth/logout.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def profile_address_save(request, template='jobauth/candidate_profile.html'):
    candidate = Candidate.objects.filter(user__id=request.user.id).first()
    address = Address.objects.filter(user__id=request.user.id).first()
    if request.method == 'POST':
        end_form = AddressForm(request.POST, instance=address)
        candidate_form = CandidateForm()

        if end_form.is_valid():
            addr = end_form.save(commit=False)
            addr.user = request.user
            addr.save()
            msg = u'Endereco cadastrado com sucesso'.encode('utf-8')
            messages.success(request, msg)
        else:
            msf_error = u'Verifique os erros a baixo.'.encode('utf-8')

            messages.error(request, msf_error)
            context = {
                'candidate_form': candidate_form,
                'address_form': end_form
            }
            return render(request, template, context)
    else:
        end_form = AddressForm(instance=address)
        candidate_form = CandidateForm(instance=candidate)
    context = {
        'candidate_form': candidate_form,
        'address_form': end_form
    }
    return render(request, template, context)


def profile_candidate_save(request, template='jobauth/candidate_profile.html'):
    candidate = Candidate.objects.filter(user__id=request.user.id).first()
    address = Address.objects.filter(user__id=request.user.id).first()
    if request.method == 'POST':
        end_form = AddressForm()
        candidate_form = CandidateForm(request.POST, instance=candidate)

        if candidate_form.is_valid():
            cand = end_form.save(commit=False)
            cand.user = request.user
            cand.save()
            msg = u'Candidto cadastrado com sucesso'.encode('utf-8')
            messages.success(request, msg)
        else:
            msf_error = u'Verifique os erros a baixo.'.encode('utf-8')

            messages.error(request, msf_error)
            context = {
                'candidate_form': candidate_form,
                'address_form': end_form
            }
            return render(request, template, context)
    else:
        end_form = AddressForm(instance=address)
        candidate_form = CandidateForm(instance=candidate)
    context = {
        'candidate_form': candidate_form,
        'address_form': end_form
    }
    return render(request, template, context)


def profile_address_delete(request, template='jobauth/candidate_profile.html'):
    candidate = Candidate.objects.filter(user__id=request.user.id).first()
    address = Address.objects.filter(user__id=request.user.id).first()
    address_form = AddressForm(instance=candidate)
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


def profile_candidate_delete(request, template='jobauth/candidate_profile.html'):
    address = Address.objects.filter(user__id=request.user.id).first()
    candidate = Candidate.objects.filter(user__id=request.user.id).first()
    address_form = AddressForm(instance=candidate)
    candidate_form = CandidateForm(instance=address)
    if request.method == 'POST':
        if address_form.is_valid():
            candidate.delete()
            msg = u'Profile deletado com sucesso'.encode('utf-8')
            messages.error(request, msg)
        else:
            msf_error = u'Formulario com suas experiencias não é valido'.encode('utf-8')
            messages.error(request, msf_error)

    context = {
        'address_form': address_form,
        'candidate_form': candidate_form
    }
    return render(request, template, context)


def profile(request):
    if request.method == 'POST':
        pass
    else:
        canidate = CandidateForm()
        end_form = AddressForm()
        context = {
            'candidate_form': canidate,
            'address_form': end_form
        }
    return render(request, 'jobauth/candidate_profile.html', context)
