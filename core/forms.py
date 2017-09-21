from django import forms

from core.models import Address, Company, Candidate


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('cep', 'endereco', 'numero', 'complemento',
                  'bairro', 'cidade', 'uf', 'observacao')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('vaga', 'salario_min', 'salario_max',
                  'experiencia', 'escolaridade', 'distancia_max')


class CandidateFrom(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('user', 'salario', 'experiencia', 'escolaridade')
