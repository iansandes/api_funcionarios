# Generated by Django 2.2.12 on 2020-12-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('matricula', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Salário')),
            ],
        ),
    ]
