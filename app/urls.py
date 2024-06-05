from django.contrib import admin
from django.urls import path
from alunos.views import home, AlunoRegisterView, AlunoLoginView, AlunoDetailView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('register/', AlunoRegisterView.as_view(), name='register'),
    path('login/', AlunoLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('aluno/<int:pk>/', AlunoDetailView.as_view(), name='aluno_detail'),
]
