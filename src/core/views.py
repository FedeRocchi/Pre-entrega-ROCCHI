from django.shortcuts import render, redirect
from . import forms, models
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request,'core/index.html')


def registar_usuarios(request):
    #forms.py
    if request.method == 'GET':
        usuario = forms.Registrar_usuarios_view()
        email = forms.Registrar_usuarios_view()
        dni = forms.Registrar_usuarios_view()
    if request.method == 'POST':
        usuario = forms.Registrar_usuarios_view(request.POST)
        email = forms.Registrar_usuarios_view(request.POST)
        dni = forms.Registrar_usuarios_view(request.POST)
        if usuario.is_valid() and email.is_valid() and dni.is_valid():
            usuario.save()
            email.save()
            dni.save()
            
    return render(request, 'core/registrar_usuario.html', {'user': usuario,'email': email,'dni': dni})

@csrf_protect
def iniciar_sesion(request):
    if request.method == 'GET':
        # Inicializa el formulario para GET
        form = forms.Iniciar_sesion_view()
        return render(request, 'core/iniciar_sesion.html', {'form': form})
    
    if request.method == 'POST':
        form = forms.Iniciar_sesion_view(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre', '')
            email = form.cleaned_data.get('email', '')
            dni = form.cleaned_data.get('dni', '')
            
            try:
                # Usa el modelo correcto
                user = models.User_register.objects.get(
                    nombre=nombre, 
                    email=email, 
                    dni=dni
                )
                return redirect('index')
            except models.User_register.DoesNotExist:
                messages.error(request, 'Credenciales incorrectas')
        
        # Si el formulario no es válido, vuelve a renderizar con los errores
        return render(request, 'core/iniciar_sesion.html', {'form': form})
# Create your views here.
