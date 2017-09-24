# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, resolve_url as r, redirect

# Create your views here.
from company.models import Company
from core.forms import AddressForm
from core.models import Address


def home(request):
    return render(request, 'core/index.html')


def address(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    try:
        addr = Address.objects.get(company__id=company.id)
    except:
        addr = Address()

    form = AddressForm(instance=addr)
    context = {
        'company': company,
        'form': form
    }
    return render(request, 'core/address/address.html', context)


def address_save(request, company_id, template='core/address/address.html'):
    company = Company.objects.get(pk=company_id)
    if request.method == 'POST':
        form = AddressForm(request.POST)
        print form
        if form.is_valid():
            addr = form.save(commit=False)
            addr.company = company
            addr.save()
            msg = u'Endereco cadastrado com sucesso'.encode('utf-8')
            messages.success(request, msg)
        else:
            msf_error = u'Verifique os erros a baixo.'.encode('utf-8')

            messages.error(request, msf_error)
            context = {
                'company': company,
                'form': form
            }
            return render(request, template, context)
    context = {
        'company': company,
        'form': form
    }
    return render(request, template, context)


def address_update(request, company_id, address_id, template='core/address/address.html'):
    _address = Address.objects.get(pk=address_id)
    company = Company.objects.get(pk=company_id)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=_address)
        print form
        if form.is_valid():
            end = form.save(commit=False)
            end.save()
            msg = u'Endereco alterado com sucesso'.encode('utf-8')
            messages.warning(request, msg)
        else:
            msf_error = u'Verifique os erros a baixo.'.encode('utf-8')

            messages.error(request, msf_error)
            context = {
                'company': company,
                'form': form
            }
            return render(request, template, context)
    context = {
        'company': company,
        'form': form
    }
    return render(request, template, context)


def address_delete(request, company_id, address_id):
    template = 'core/address/address.html'
    _address = Address.objects.get(pk=address_id)
    company = Company.objects.get(pk=company_id)
    if request.method == 'POST':
        _address.delete()
        msg = u'Endereço foi deletado com sucesso'.encode('utf-8')
        messages.error(request, msg)

    return redirect(r('company:company_list'))
