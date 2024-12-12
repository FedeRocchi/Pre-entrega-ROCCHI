
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('registrar_usuario/', views.registar_usuarios, name='registrar'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion')
]