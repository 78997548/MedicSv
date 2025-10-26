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
