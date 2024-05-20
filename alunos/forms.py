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

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Senhas não identicas!')
        return password2
