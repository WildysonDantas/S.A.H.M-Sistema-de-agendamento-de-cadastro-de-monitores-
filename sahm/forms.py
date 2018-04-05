# _*_ coding: utf-8 _*_
from django import forms
from django.forms import ModelForm
from .models import Monitor

class MonitorModelForm(forms.ModelForm):

    class Meta:
        model = Monitor
        fields = ('nome', 'matricula', 'email', 'telefone', 'curso', 'nascimento', 'senha')
        widgets = {
            'nome':forms.TextInput(attrs={'name':'nome', 'placeholder':'Informe o seu nome completo','id':'id_nome', 'class':'form-control', 'required':True}),
            'matricula':forms.NumberInput(attrs={'name':'matricula', 'id':'id_matricula', 'class':'form-control', 'required':True}),
            'email':forms.EmailInput(attrs={'name':'email', 'id':'id_email', 'class':'form-control', 'data-error':'Por favor, informe um e-mail correto.', 'required':True}),
            'telefone':forms.NumberInput(attrs={'name':'telefone', 'id':'id_fone', 'class':'form-control', 'placeholder':'DDD+Número', 'required':True}),
            'curso':forms.Select(attrs={'name':'curso', 'class':'selectpicker form-control','id':'select_curso','required':True}, choices=(('1','CSHNB - ADMINISTRAÇÃO'), ('2','CSHNB - CIÊNCIAS BIOLÓGICAS'),('3','CSHNB - ENFERMAGEM'),('4', 'CSHNB - HISTÓRIA'), ('5', 'CSHNB - LETRAS'),
            ('6','CSHNB - MATEMÁTICA'),('7','CSHNB - MEDICINA'),('8','CSHNB - NUTRIÇÃO'), ('9','CSHNB - PEDAGOGIA'), ('10','CSHNB - SISTEMAS DE INFORMAÇÃO'))),
            'nascimento':forms.DateInput(attrs={'type':'date','name':'nascimento', 'id':'id_nascimento', 'class':'form-control', 'required':True}),
            'senha':forms.PasswordInput(attrs={'name':'senha', 'id':'id_senha', 'class':'form-control', 'data-minlength':6, 'required':True}),
        }
