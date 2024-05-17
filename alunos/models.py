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
