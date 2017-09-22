from django.contrib import admin
from core.models import Company, Job, Candidate
from core.forms import JobForm, CompanyForm, CandidateForm

# Register your models here.
from jobauth.models import Profile


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

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    form = CandidateForm

