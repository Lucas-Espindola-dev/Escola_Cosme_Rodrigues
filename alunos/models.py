from django.db import models
from django.contrib.auth.models import AbstractUser


SERIES_CHOICES = (
    (8, 'Oitavo ano'),
    (9, 'Nono Ano'),
)


class Aluno(AbstractUser):
    date_joined = None
    first_name = None
    last_name = None

    username = models.CharField(
        verbose_name='Nome do Usuario',
        max_length=255,
        unique=True,
    )
    email = models.EmailField(verbose_name='E-mail', max_length=255)
    full_name = models.CharField(verbose_name='Nome Completo', max_length=255)
    matricula = models.IntegerField(verbose_name='Matrícula', unique=True)
    seduc = models.CharField(verbose_name='Senha Seduc', max_length=255)
    cpf = models.IntegerField(verbose_name='CPF', unique=True, blank=True, null=True)
    serie = models.IntegerField(verbose_name='Série do aluno', choices=SERIES_CHOICES)
    telefone = models.IntegerField(verbose_name='Telefone', unique=True, blank=True, null=True)
    mother_name = models.CharField(verbose_name='Nome da mãe', max_length=255, blank=True, null=True)
    father_name = models.CharField(verbose_name='Nome da pai', max_length=255, blank=True, null=True)
