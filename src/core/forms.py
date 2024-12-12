from django import forms
from . import models

class Registrar_usuarios_view(forms.ModelForm):
    class Meta:
        model = models.User_register
        
        fields = ['nombre', 'email', 'dni']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '')
       #
        if len(nombre) < 3:
            raise forms.ValidationError("La longitud del nombre, debe ser mayor a 3 caracteres")
        if not nombre.isalpha():
            raise forms.ValidationError('El nombre solo debe tener letras, no puede contener numeros')
       
        return  nombre
    def clean_dni(self):
        dni = self.cleaned_data.get('dni', '')

        if not (7 <= len(str(dni)) <= 10):
            raise forms.ValidationError('El DNI debe ser entre 7 a 10 digitos')
        return dni


    
class Iniciar_sesion_view(forms.ModelForm):
    class Meta:
        model = models.User_register
        fields = ['nombre', 'email', 'dni']

        