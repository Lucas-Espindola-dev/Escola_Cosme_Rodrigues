from django.contrib import admin
from django.urls import path
from alunos.views import home, AlunoRegisterView, AlunoLoginView, AlunoDetailView, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('register/', AlunoRegisterView.as_view(), name='register'),
    path('login/', AlunoLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('aluno/', AlunoDetailView.as_view(), name='aluno_detail'),
]
