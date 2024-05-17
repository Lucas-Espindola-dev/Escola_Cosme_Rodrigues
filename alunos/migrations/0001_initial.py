# Generated by Django 5.0.6 on 2024-05-17 12:43

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Nome do Usuario')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('full_name', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('matricula', models.IntegerField(unique=True, verbose_name='Matrícula')),
                ('seduc', models.CharField(max_length=255, verbose_name='Senha Seduc')),
                ('cpf', models.IntegerField(blank=True, null=True, unique=True, verbose_name='CPF')),
                ('serie', models.IntegerField(choices=[(8, 'Oitavo ano'), (9, 'Nono Ano')], verbose_name='Série do aluno')),
                ('telefone', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Telefone')),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome da mãe')),
                ('father_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome da pai')),
                ('is_active', models.BooleanField(default=True, help_text='Desmarque essa opção para desativar o usuário e impedir o login.', verbose_name='Ativo')),
                ('is_staff', models.BooleanField(default=False, help_text='Marque essa opção para conceder acesso a área administrativa.', verbose_name='Admin')),
                ('is_superuser', models.BooleanField(default=False, help_text='Marque essa opção para conceder todos os privilégios, sem a necessidade de permissões.', verbose_name='Superusuário')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'db_table': 'alunos_cosme_rodrigues',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]