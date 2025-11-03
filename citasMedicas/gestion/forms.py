from django import forms
from .models import Paciente, Medico, Cita

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'

class LoginForm(forms.Form):
    usuario= forms.CharField(max_length=50, label='Usuario')
    contraseña= forms.CharField(max_length=50, widget=forms.PasswordInput, label='Contraseña')
    
class RegisterForm(forms.Form):
    usuario=forms.CharField(max_length=50, label='usario')
    contraseña=forms.CharField(max_length=50, widget=forms.PasswordInput, label='contraseña')
     