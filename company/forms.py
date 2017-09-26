from django import forms

from company.models import Company, Job


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name',)


class JobForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company')
        super(JobForm,self).__init__(*args, **kwargs)
        self.fields['company'].empty_label = None
        self.fields['company'].queryset = Company.objects.filter(pk=company.id)

    class Meta:
        model = Job
        fields = ('company', 'name', 'description', 'salario_min', 'salario_max',
                  'experiencia', 'escolaridade', 'distancia_max',)

