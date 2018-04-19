from django.shortcuts import render, redirect
from .models import Monitor
from .forms import UserModelForm
from .forms import MonitorModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect



# Create your views here.

def cadastrar_monitor(request):

    form = UserModelForm(request.POST or None)
    form_monitor = MonitorModelForm(request.POST or None)
    context = {'form':form, 'form_monitor':form_monitor}
    if request.method == "POST":
        if form.is_valid():
            try:
                monitor_email = User.objects.get(email=request.POST.get('email'))
                monitor_username = User.objects.get(username=request.POST.get('matricula'))

                if monitor_email or monitor_username:
                    return render(request, 'sahm/cadastroMonitor.html', {'msg': 'Matricula ou email já cadastrados'})

            except User.DoesNotExist:

                user = form.save(commit=False)
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user.set_password(password)

                user.save()
                return redirect('/acesso', context)

    return render(request, 'sahm/cadastroMonitor.html', context)

def monitor_login(request):

    if request.method == "POST":
        
        monitor_consulta = User.objects.get(email=request.POST.get('email'))
        monitor = authenticate(username=monitor_consulta.username, password=request.POST.get('password'))

        if monitor is not None:
            if monitor.is_active:
                login(request, monitor)
                return HttpResponseRedirect('/acesso', {'monitor':monitor_consulta})
        else:
            return HttpResponseRedirect('/login')

    return render(request, 'sahm/login.html')

@login_required
def monitor_logout(request):
    logout(request)
    return render(request, 'sahm/login.html', {})

@login_required
def acesso_monitor(request):
    return render(request, 'viewMonitor.html')

@login_required
def dados_cadastrais_monitor(request):

    user = User.objects.get(username= request.user.username)
    form = UserModelForm(request.POST or None, initial={'first_name':user.first_name, 'username':user.username})
    form_monitor = MonitorModelForm(request.POST or None, initial={'telefone': user.monitor.telefone, 'nascimento':user.monitor.nascimento,'curso': user.monitor.curso})
    context = {'form_monitor':form_monitor, 'form':form}

    if request.method == "POST":
        if form_monitor.is_valid() and form.is_valid():
            if request.user.is_authenticated:

                #user.first_name = form.cleaned_data['first_name']
                #user.username = form.cleaned_data['username']
                user.monitor.telefone = form_monitor.cleaned_data.get('telefone')
                user.monitor.nascimento = form_monitor.cleaned_data.get('nascimento')
                user.monitor.curso = form_monitor.cleaned_data.get('curso')
                user.save()

            else:
                return redirect('/acesso')


    return render(request, 'sahm/updateMonitor.html', context)
