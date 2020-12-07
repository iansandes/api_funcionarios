from django.db import models

class Funcionario(models.Model):
    matricula = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField("Nome", max_length=50)
    salario = models.DecimalField("Salário", max_digits=20, decimal_places=2)
