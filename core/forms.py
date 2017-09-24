# -*- coding: utf-8 -*-
from django import forms

from core.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('cep', 'endereco', 'numero', 'complemento',
                  'bairro', 'cidade', 'uf', 'observacao',)

