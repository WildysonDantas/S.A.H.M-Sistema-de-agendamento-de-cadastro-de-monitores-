from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Monitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    #nome = models.CharField(max_length=250)
    #matricula = models.BigIntegerField()
    #email = models.EmailField()
    telefone = models.BigIntegerField(null=True, blank=True)
    curso = models.CharField(max_length=200, null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True)
    #senha = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def criar_monitor(sender, instance, created, **kwargs):
    if created:
        Monitor.objects.create(user=instance)

@receiver(post_save, sender=User)
def salvar_monitor(sender, instance, **kwargs):
    instance.monitor.save()
