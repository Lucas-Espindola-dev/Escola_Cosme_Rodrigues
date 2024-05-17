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

    is_active = models.BooleanField(
        verbose_name='Ativo',
        default=True,
        help_text='Desmarque essa opção para desativar o usuário e impedir o login.',
    )
    is_staff = models.BooleanField(
        verbose_name="Admin",
        default=False,
        help_text="Marque essa opção para conceder acesso a área administrativa.",
    )
    is_superuser = models.BooleanField(
        verbose_name="Superusuário",
        default=False,
        help_text="Marque essa opção para conceder todos os privilégios, sem a necessidade de permissões."
    )

    REQUIRED_FIELDS = ['email', 'full_name']
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        db_table = 'alunos'

    def __str__(self):
        return self.full_name
