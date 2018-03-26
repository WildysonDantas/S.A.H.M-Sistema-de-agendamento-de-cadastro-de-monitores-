from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cadastrar_monitor, name='cadastrar_monitor'),
]
