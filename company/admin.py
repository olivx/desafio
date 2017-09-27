from django.contrib import admin

# Register your models here.
from company.forms import JobForm
from company.models import Company, Job


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'address',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_filter = ('distancia_max', 'experiencia', 'escolaridade')
    list_display = ('name', 'experiencia', 'escolaridade', 'distancia_max',
                    'salario_min', 'salario_max')