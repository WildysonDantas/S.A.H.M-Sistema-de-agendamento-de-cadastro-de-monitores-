from django.shortcuts import render, redirect
from .models import Monitor
from .forms import UserModelForm
from .forms import MonitorModelForm
#from .forms import EmailUpdateModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
#from django.contrib.auth.hashers


# Create your views here.

def tela_inicial(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def horario(request):
    return render(request, 'funcionamento.html')

def contato(request):
    return render(request, 'contato.html')

def cadastrar_monitor(request):

    form = UserModelForm(request.POST or None)
    if request.method == "POST":
        #form_monitor = MonitorModelForm(request.POST or None)

        if form.is_valid():

            try:
                monitor_username = User.objects.get(username=request.POST.get('matricula'))
                context = {
                    'form':form,
                    'msg_matricula': 'Matricula já cadastrada!'
                }
                return render(request, 'sahm/cadastroMonitor.html', context)

            except User.DoesNotExist:
                monitor_email = User.objects.filter(email=request.POST.get('email')).count()
                if monitor_email:
                    context = {
                        'form':form,
                        'msg_email': 'Email já cadastrado!'
                    }
                    return render(request, 'sahm/cadastroMonitor.html', context)
                else:

                    user = form.save(commit=False)
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    user.set_password(password)
                    user.save()
                    return render(request, 'sahm/login.html')
    else:
        form = UserModelForm()

    context = {'form':form}
    return render(request, 'sahm/cadastroMonitor.html', context)

def monitor_login(request):

    if request.method == "POST":

        try:
            monitor_consulta = User.objects.get(email=request.POST.get('email'))
            monitor = authenticate(username=monitor_consulta.username, password=request.POST.get('password'))

            if monitor is not None:
                if monitor.is_active:
                    login(request, monitor)
                    return HttpResponseRedirect('/acesso', {'monitor':monitor_consulta})
            else:
                return render(request, 'sahm/login.html', {'msg':'Senha Inválida !'})
        except User.DoesNotExist:
            return render(request, 'sahm/login.html', {'msg':'Monitor não Cadastrado !'})

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
    form_monitor = MonitorModelForm(request.POST or None, initial={'telefone': user.monitor.telefone, 'nascimento':user.monitor.nascimento,'curso': user.monitor.curso}, prefix="moni")
    context = {'form_monitor':form_monitor}

    if request.method == "POST":
        if form_monitor.is_valid():
            if request.user.is_authenticated:

                if request.POST['nome'] != '':
                    user.first_name = request.POST['nome']

                user.monitor.telefone = form_monitor.cleaned_data.get('telefone')
                user.monitor.nascimento = form_monitor.cleaned_data.get('nascimento')
                user.monitor.curso = form_monitor.cleaned_data.get('curso')
                user.save()
                context = {'form_monitor':form_monitor, 'user':user, 'msg':'Dados Alterados Com Sucesso!'}
                return render(request, 'sahm/updateMonitor.html', context)

            else:
                return redirect('/acesso')

        else:
            return redirect('/acesso')

    return render(request, 'sahm/updateMonitor.html', context)

@login_required
def dados_principal_monitor(request):

    user = User.objects.get(username= request.user.username)
    form = UserModelForm(request.POST or None, initial={'first_name':user.first_name, 'username':user.username, 'email':user.email}, prefix="usr")
    context = {'form':form}

    if request.method == "POST":

        if form.is_valid():
            #user.username = form.cleaned_data.get('username')
            #user.first_name = form.cleaned_data.get('first_name')
            #user.save()
            user.update(username=form.cleaned_data.get('username'))
            user.update(first_name=form.cleaned_data.get('first_name'))
        else:
            return redirect('/acesso', context)
    else:
        return render(request, 'sahm/updateUserMonitor.html', context)

@login_required
def update_password(request):

    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/dados_principal_monitor')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('/mudar_senha')

    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'sahm/updatePassword.html', {'form': form})

@login_required
def update_email(request):

    user = User.objects.get(username= request.user.username)
    context = {'user':user}

    if request.method == "POST":
        if user.check_password(request.POST['password']):
            user.email = request.POST['email']
            user.save()
            context = {'user':user, 'msg':'Email Alterado com Sucesso !'}
            return render(request, 'sahm/updateEmail.html', context)
        else:
            return redirect('/acesso')

    return render(request, 'sahm/updateEmail.html', context)

@login_required
def excluir_conta(request):

    User.objects.get(username= request.user.username).delete()
    messages.success(request, "The user is deleted")
    logout(request)
    return render(request, 'sahm/login.html', {})
