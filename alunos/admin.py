from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Aluno


class CustomAlunoAdmin(UserAdmin):
    list_display = ['id', 'full_name', 'username', 'matricula', 'email', 'is_active', 'is_staff']
    list_display_links = ['id', 'full_name', 'username', 'matricula', ]
