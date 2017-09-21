from django.contrib import admin
from core.models import Company
from core.forms import CompanyForm


# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm

    search_fields = ('vaga',)
    list_filter = ('distancia_max','experiencia', 'escolaridade')
    list_display = ('vaga', 'experiencia', 'escolaridade', 'distancia_max',
                    'salario_min', 'salario_max')
