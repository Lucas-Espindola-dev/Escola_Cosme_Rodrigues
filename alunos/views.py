from django.shortcuts import render, redirect
from django.views import View
from .forms import AlunoCreationForm


def home(request):
    return render(request, 'pages/home.html')


class AlunoRegisterView(View):
    form_class = AlunoCreationForm
    initial = {'key': 'value'}
    template_name = 'pages/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})


