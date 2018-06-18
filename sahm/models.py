from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


# Create your models here.

class Monitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True)
    #nome = models.CharField(max_length=250)
    #matricula = models.BigIntegerField()
    #email = models.EmailField()
    telefone = models.BigIntegerField(null=True, blank=True)
    curso = models.CharField(max_length=200, null=True, blank=True)
    materia =  models.CharField(max_length=200, null=True, blank=True)
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

class Monitoria(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='monitoria')
    dia = models.DateField(u'Dia da Monitoria', help_text=u'Dia da Monitoria', null=True, blank=True)
    hora_inicio = models.TimeField(u'Hora de Inicio', help_text=u'Hora de Inicio', null=True, blank=True)
    hora_termino = models.TimeField(u'Hora de Termino', help_text=u'Hora de Termino', null=True, blank=True)
    sala = models.IntegerField(null=True, blank=True)

    def check_overlap(self, hora_inicio, hora_termino, novo_inicio, novo_fim):
        overlap = False

        if novo_inicio == hora_termino or novo_fim == hora_inicio:
            overlap = False
        elif (novo_inicio >= hora_inicio and novo_inicio <= hora_termino) or (novo_fim >= hora_inicio and novo_fim <= hora_termino): #innner limits
            overlap = True
        elif novo_inicio <= hora_inicio and novo_fim >= hora_termino:
            overlap = True

        return overlap

    def clean (self):
        if self.hora_termino <= self.hora_inicio:
            raise ValidationError('Tempo de término menor que o Tempo de inicio.')

        #events = Monitoria.objects.filter(dia=self.dia)
        #if events.exists():
            #if self.check_overlap(events.hora_inicio, events.hora_termino, self.hora_inicio, self.hora_termino):
                #raise ValidationError('There is an overlap with another event: ' + str(events.dia) + ', ' + str(events.hora_inicio) + '-' + str(events.hora_termino))

    def __str__(self):
        return str(self.user)

    #@receiver(post_save, sender=User)
    #def criar_monitoria(sender, instance, created, **kwargs):
    #    if created:
    #        Monitoria.objects.create(user=instance)

    #@receiver(post_save, sender=User)
    #def salvar_monitoria(sender, instance, **kwargs):
    #    instance.monitoria.save()
