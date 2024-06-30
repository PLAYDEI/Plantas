from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'nombre', 'apellido', 'email', 'contraseña']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'contraseña']