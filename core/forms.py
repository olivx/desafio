from django import forms

from core.models import Address, Company, Candidate


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('cliente', 'cep', 'endereco', 'numero', 'complemento',
                  'bairro', 'cidade', 'uf', 'observacao')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('end', 'vaga', 'salario_min', 'salario_max',
                  'experiencia', 'escolariodade', 'distancia_max')


class CandidateFrom(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('end', 'user', 'salario', 'experiencia', 'scolariodade')
