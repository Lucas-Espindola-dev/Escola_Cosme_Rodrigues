from django.shortcuts import render
from django.views import View
from .forms import AlunoCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'pages/home.html')


class AlunoRegisterView(View):
    form_class = AlunoCreationForm
    initial = {'key': 'value'}
    template_name = 'pages/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)


class AlunoLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'pages/login.html'


