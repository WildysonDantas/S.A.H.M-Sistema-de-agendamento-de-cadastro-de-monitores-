from django.db import models
from django.utils import timezone

# Create your models here.

class Monitor(models.Model):
    nome = models.CharField(max_length=250)
    matricula = models.BigIntegerField()
    email = models.EmailField()
    telefone = models.BigIntegerField()
    curso = models.CharField(max_length=200)
    periodo = models.PositiveSmallIntegerField()
    nascimento = models.DateField()
    senha = models.CharField(max_length=200)

    def __str__(self):
        return self.matricula
