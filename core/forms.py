from django import forms

from core.models import Address, Company, Candidate, Job


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('cep', 'endereco', 'numero', 'complemento',
                  'bairro', 'cidade', 'uf', 'observacao',)


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', )


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('company', 'name', 'description', 'salario_min', 'salario_max',
                  'experiencia', 'escolaridade', 'distancia_max',)


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('salario', 'experiencia', 'escolaridade',)
