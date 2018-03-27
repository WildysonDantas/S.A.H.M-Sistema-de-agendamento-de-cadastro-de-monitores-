from django.shortcuts import render
from .models import Monitor
from .forms import MonitorForm
# Create your views here.

def cadastrar_monitor(request):

    data = {}
    if request.method == "POST":
        data['nome'] = request.POST.get('nome', 'nome não encontrado')
        data['matricula'] = request.POST.get('matricula', 'matricula não encontrada')
        data['email'] = request.POST.get('email', 'email não encontrado')
        data['telefone'] = request.POST.get('telefone', 'telefone não encontrado')
        data['curso'] = request.POST.get('curso', 'curso não encontrado')
        data['periodo'] = request.POST.get('periodo', 'periodo não encontrado')
        data['nascimento'] = request.POST.get('nascimento', 'data de nascimento não encontrada')
        data['senha'] = request.POST.get('senha', 'senha não encontrada')
        data['confirmaSenha'] = request.POST.get('confirmaSenha', 'senha não encontrada')

        if (data['senha'] == data['confirmaSenha']):
            monitor = Monitor.objects.create(nome=data['nome'], matricula=data['matricula'], email=data['email'],
            telefone=data['telefone'], curso=data['curso'], periodo=data['periodo'], nascimento=data['nascimento'],
            senha=data['senha'])
            return render(request, 'sahm/viewMonitor.html', {'monitor' : monitor})


    return render(request, 'sahm/cadastroMonitor.html', data)

def login(request):
    return render(request, 'sahm/login.html', {})

def acesso_monitor(request):
    return render(request, 'sahm/viewMonitor.html', {})
