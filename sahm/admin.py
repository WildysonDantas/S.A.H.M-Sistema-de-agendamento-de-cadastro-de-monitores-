from django.contrib import admin
from .models import Monitor
from .models import Monitoria

# Register your models here.
admin.site.register(Monitor)
admin.site.register(Monitoria)
