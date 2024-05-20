# Generated by Django 5.0.6 on 2024-05-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Matrícula'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='seduc',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Senha Seduc'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='serie',
            field=models.IntegerField(blank=True, choices=[(8, 'Oitavo ano'), (9, 'Nono Ano')], null=True, verbose_name='Série do aluno'),
        ),
    ]