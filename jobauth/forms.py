from django import forms
from cuser.models import CUser
from cuser.forms import UserCreationForm
from jobauth.models import Profile, Candidate


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Nome', max_length=30, required=False, help_text='Opicional.')
    last_name = forms.CharField(label='Sobre Nome', max_length=30, required=False, help_text='Opicional.')
    type = forms.ChoiceField(label='Empresa ou Candidato ?', choices=Profile.KIND_USER, initial=Profile.EMPLOYEE,
                             required=True, widget=forms.Select())

    class Meta:
        model = CUser
        fields = ('email', 'first_name', 'last_name', 'type',
                  'password1', 'password2',)




class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('last_job', 'salario', 'experiencia', 'escolaridade',)
