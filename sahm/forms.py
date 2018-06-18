# _*_ coding: utf-8 _*_
from django import forms
from django.forms import ModelForm
from .models import Monitor
from .models import Monitoria
from django.contrib.auth.models import User


class UserModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password')
        widgets = {
            'first_name':forms.TextInput(attrs={'name':'nome', 'placeholder':'Informe o seu nome completo','id':'id_nome', 'class':'form-control', 'required':True}),
            'username':forms.TextInput(attrs={'type':'number', 'name':'matricula', 'id':'id_matricula', 'class':'form-control', 'data-maxlength': 11, 'data-minlength': 11, 'required':True}),
            'email':forms.EmailInput(attrs={'name':'email', 'id':'id_email', 'class':'form-control', 'data-error':'Por favor, informe um e-mail correto.', 'required':True}),
            'password':forms.PasswordInput(attrs={'name':'senha', 'id':'id_senha', 'class':'form-control', 'data-minlength':6, 'required':True}),
        }


class MonitorModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MonitorModelForm, self).__init__(*args, **kwargs)
        self.fields['telefone'].initial = self.instance.telefone


    class Meta:
        model = Monitor
        fields = ('telefone', 'curso', 'nascimento', 'materia')
        widgets = {
            'telefone':forms.NumberInput(attrs={'name':'telefone', 'id':'id_fone', 'class':'form-control', 'placeholder':'DDD+Número'}),
            'curso':forms.Select(attrs={'name':'curso', 'class':'selectpicker form-control','id':'select_curso'}, choices=(('1','CSHNB - ADMINISTRAÇÃO'), ('2','CSHNB - CIÊNCIAS BIOLÓGICAS'),('3','CSHNB - ENFERMAGEM'),('4', 'CSHNB - HISTÓRIA'), ('5', 'CSHNB - LETRAS'),
            ('6','CSHNB - MATEMÁTICA'),('7','CSHNB - MEDICINA'),('8','CSHNB - NUTRIÇÃO'), ('9','CSHNB - PEDAGOGIA'), ('10','CSHNB - SISTEMAS DE INFORMAÇÃO'))),
            'nascimento':forms.DateInput(attrs={'type':'date','name':'nascimento', 'id':'id_nascimento', 'class':'form-control'}),
            'materia':forms.TextInput(attrs={'type':'text', 'name':'materia', 'id':'id_materia', 'class':'form-control', 'required':True})
        }

class MonitoriaModelForm(forms.ModelForm):
    class Meta:
        model = Monitoria
        fields = ('dia', 'hora_inicio', 'hora_termino', 'sala')
        widgets = {
            'dia':forms.DateInput(attrs={'id':'id_dia', 'name':'dia', 'class':'form-control', 'placeholder':'DD/MM/YYYY', 'type':'date', 'required':True}),
            'sala':forms.NumberInput(attrs={'id':'id_sala', 'name':'sala', 'placeholder':'Nº da Sala', 'class':'form-control input-md', 'required':True}),
            'hora_inicio':forms.TextInput(attrs={'id':'id_hora_inicio', 'name':'hora_inicio', 'type':'time', 'class':'form-control input-md', 'required':True}),
            'hora_termino':forms.TextInput(attrs={'id':'id_hora_termino', 'name':'hora_termino', 'type':'time', 'class':'form-control input-md', 'required':True}),
        }

#class EmailUpdateModelForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ('email')
#        widgets = {
#            'email':forms.EmailInput(attrs={'name':'email', 'id':'id_email', 'class':'form-control', 'data-error':'Por favor, informe um e-mail correto.', 'required':True}),
#        }
