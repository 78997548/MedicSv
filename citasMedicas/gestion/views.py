from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Medico, Cita
from .forms import PacienteForm, MedicoForm, CitaForm

# ---------- PACIENTES ----------
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})

def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/form.html', {'form': form})

def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/form.html', {'form': form})

def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista_pacientes')
    return render(request, 'pacientes/confirm_delete.html', {'obj': paciente})

# ---------- MEDICOS ----------
def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos/lista.html', {'medicos': medicos})

def crear_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_medicos')
    else:
        form = MedicoForm()
    return render(request, 'medicos/form.html', {'form': form})

def editar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('lista_medicos')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'medicos/form.html', {'form': form})

def eliminar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    if request.method == 'POST':
        medico.delete()
        return redirect('lista_medicos')
    return render(request, 'medicos/confirm_delete.html', {'obj': medico})

# ---------- CITAS ----------
def lista_citas(request):
    citas = Cita.objects.select_related('paciente', 'medico').all()
    return render(request, 'citas/lista.html', {'citas': citas})

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm()
    return render(request, 'citas/form.html', {'form': form})

def editar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'citas/form.html', {'form': form})

def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        cita.delete()
        return redirect('lista_citas')
    return render(request, 'citas/confirm_delete.html', {'obj': cita})
