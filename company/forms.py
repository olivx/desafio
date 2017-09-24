from django import forms

from company.models import Company, Job


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', )


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('company', 'name', 'description', 'salario_min', 'salario_max',
                  'experiencia', 'escolaridade', 'distancia_max',)
