from django import forms
from .models import Aluno


class AlunoCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Aluno
    fields = ('username', 'email', 'full_name',
              'matricula', 'seduc', 'cpf', 'serie',
              'telefone', 'mother_name', 'father_name',)
