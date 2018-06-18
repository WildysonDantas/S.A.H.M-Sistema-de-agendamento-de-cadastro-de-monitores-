from django.conf.urls import url
from . import views

app_name = 'sahm'
urlpatterns = [
    url(r'^$', views.tela_inicial, name='index'),
    url(r'^sobre/$', views.sobre, name='sobre'),
    url(r'^como_funciona/$', views.horario, name='horario'),
    url(r'^contate-nos/$', views.contato, name='contato'),
    url(r'^login/$', views.monitor_login, name='login'),
    url(r'^cadastro/$', views.cadastrar_monitor, name='cadastrar_monitor'),
    url(r'^monitoria_cadastro/$', views.cadastro_monitoria, name='cadastro_monitoria'),
    url(r'^monitoria/$', views.feed_monitoria, name='feed_monitoria'),
    url(r'^acesso/$', views.acesso_monitor, name="acesso_monitor"),
    url(r'^logout/$', views.monitor_logout, name="logout"),
    url(r'^dados_cadastrais_monitor/$', views.dados_cadastrais_monitor, name='dados_cadastrais_monitor'),
    url(r'^dados_principal_monitor/$', views.dados_principal_monitor, name='dados_principal_monitor'),
    url(r'^mudar_senha/$', views.update_password, name='update_password'),
    url(r'^mudar_email/$', views.update_email, name='update_email'),
    url(r'^excluir_conta/$', views.excluir_conta, name='excluir_conta'),
]
