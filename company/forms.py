from django import forms

from company.models import Company, Job


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name',)


class JobForm(forms.ModelForm):
    # def __init__(self, user_id=0, *args, **kwargs):
    #     super(JobForm, self).__init__(*args, **kwargs)
    #     if user_id is not 0:
    #         self.fields['company'].queryset =\
    #                 Company.objects.filter(user_id=user_id)


    class Meta:
        model = Job
        fields = ('company', 'name', 'description', 'salario_min', 'salario_max',
                  'experiencia', 'escolaridade', 'distancia_max',)
