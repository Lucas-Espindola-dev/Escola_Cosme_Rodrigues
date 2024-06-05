from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views import View
from .forms import AlunoCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import DetailView
from .models import Aluno


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
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(nome=username, password=raw_password)
            return redirect('login')
        return render(request, self.template_name, {'form': form})


class AlunoLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'pages/login.html'

    def get_success_url(self):
        return reverse_lazy('aluno_detail')


class AlunoDetailView(LoginRequiredMixin, DetailView):
    model = Aluno
    template_name = 'pages/aluno_detail.html'
    context_object_name = 'aluno'

    def get_object(self, queryset=None):
        return get_object_or_404(Aluno, pk=self.request.user.pk)
