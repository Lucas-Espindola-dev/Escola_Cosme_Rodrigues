from django.contrib import admin
from django.urls import path
from alunos.views import home, AlunoRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('register/', AlunoRegisterView.as_view(), name='register'),
]
