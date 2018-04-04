from django import forms
from .models import Monitor

class MonitorForm(forms.ModelForm):

    class Meta:
        model = Monitor
        fields = ('nome', 'matricula', 'email', 'telefone', 'curso', 'nascimento')
