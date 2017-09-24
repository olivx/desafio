from django import forms

from core.models import Address, Candidate

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('cep', 'endereco', 'numero', 'complemento',
                  'bairro', 'cidade', 'uf', 'observacao',)



class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('salario', 'experiencia', 'escolaridade',)
