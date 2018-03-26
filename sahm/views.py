from django.shortcuts import render
from .models import Monitor
# Create your views here.

def cadastrar_monitor(request):
    return render(request, 'sahm/cadastroMonitor.html', {})
