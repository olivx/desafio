from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from core.forms import CandidateForm
from core.models import Candidate


# Create your views here.

def home(request):
    return render(request, 'core/index.html')


def profile_save(request, pk):

    obj = Candidate.objects.get(user__id=pk)
    form = CandidateForm(request.POST or None, instance=obj)
    print obj
    if request.method == 'POST':
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.user = request.user
            candidate.save()
            messages.success(request, 'Perfil savo com sucesso.')
        else:
            messages.error(request, 'Foram encontrados erros durante o processamento.')

    else:
        form = CandidateForm(instance=obj)
    return render(request, 'core/candidate/candidate_profile.html', {'form': form})

