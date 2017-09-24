from django.contrib import admin

# Register your models here.
from core.forms import CandidateForm
from core.models import Candidate


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    form = CandidateForm

