from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'pages/home.html')


