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
                form_monitor.save()
                return render(request, 'sahm/viewMonitor.html', context)

    return render(request, 'sahm/cadastroMonitor.html', context)

def monitor_login(request):

    if request.method == "POST":
        monitor_consulta = User.objects.get(email=request.POST.get('email'))
        monitor = authenticate(username=monitor_consulta.username, password=request.POST.get('password'))

        if monitor is not None:
            if monitor.is_active:
                login(request, monitor)
                return HttpResponseRedirect('/acesso')
        else:
            return HttpResponseRedirect('/cadastro')

    return render(request, 'sahm/login.html')

@login_required
def monitor_logout(request):
    logout(request)
    return render(request, 'sahm/login.html', {})

@login_required
def acesso_monitor(request):
    return render(request, 'sahm/viewMonitor.html')
