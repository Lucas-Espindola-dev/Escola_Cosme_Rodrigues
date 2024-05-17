from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Aluno


class CustomAlunoAdmin(UserAdmin):
    list_display = ['id', 'full_name', 'username', 'matricula', 'email', 'is_active', 'is_staff']
    list_display_links = ['id', 'full_name', 'username', 'matricula', ]
    list_filter = ['is_active', 'is_staff', 'is_superuser', ]
    search_fields = ['full_name', 'username', 'matricula', ]
    ordering = ['full_name', 'username', ]
    actions = ['activate_users', 'deactivate_users']
    fieldsets = (
        ("Informações de Acesso", {
            "fields": (
                "username",
                "password"
            )
        }),
        ("Informações Pessoais", {
            "fields": (
                "full_name",
                "matricula",
                "email",
                "seduc",
                "cpf",
                "serie",
                "telefone",
                "mother_name",
                "father_name",
            )
        }),
        ("Permissões", {
            "fields": (
                "groups",
                "user_permissions",
                "is_active",
                "is_staff",
                "is_superuser",
            )
        }),
    )

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    activate_users.short_description = "Ativar Usuários"

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_users.short_description = "Desativar Usuários"


admin.site.register(Aluno, CustomAlunoAdmin)
