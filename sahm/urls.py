from django.conf.urls import url
from . import views

app_name = 'sahm'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^cadastro/$', views.cadastrar_monitor, name='cadastrar_monitor'),
    url(r'^acesso/$', views.acesso_monitor, name="acesso_monitor"),
]
