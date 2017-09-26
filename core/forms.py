# -*- coQueryDictding: utf-8 -*-
from django import forms

from core.models import Address


class AddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company')
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['company'].initial = company

    company = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Address
        fields = ('cep', 'endereco', 'numero', 'complemento',
                  'bairro', 'cidade', 'uf', 'observacao',)
