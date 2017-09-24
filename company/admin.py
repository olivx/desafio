from django.contrib import admin

# Register your models here.
from company.forms import CompanyForm, JobForm
from company.models import Company, Job


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm
    search_fields = ('name',)
    list_display = ('name',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    form = JobForm

    search_fields = ('name', 'description')
    list_filter = ('distancia_max', 'experiencia', 'escolaridade')
    list_display = ('name', 'experiencia', 'escolaridade', 'distancia_max',
                    'salario_min', 'salario_max')