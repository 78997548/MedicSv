from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Medico, Cita
from .forms import PacienteForm, MedicoForm, CitaForm
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#pagina principal (login)
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('un')
        password=request.POST.get('pw')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login (request, user )
            return redirect('menu')
    return render(request, 'principal/login.html')



def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('un')
        password = request.POST.get('pw')
        # Crear nuevo usuario
        user = User.objects.create_user(username=username, password=password)
        # Iniciar sesión automáticamente
        login(request, user)
        return redirect('menu')
    return render(request, 'principal/registro.html')
  
    
#logout
def logout_view(request):
    logout(request)
    return redirect('login')


def menu_view(request):
    return render(request, 'principal/menu.html')

    
        
    
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
#se construira un logica para mostrar los medicos que esten en la platforma y se diferenciaran por medio de sus especialidades

def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos/medicos.html', {'medicos': medicos})

# ---------- CITAS ----------
def lista_citas(request):
    citas = Cita.objects.select_related('medico').all()
    medicos = Medico.objects.all()

    if request.method == 'POST':
        medico_id = request.POST.get('medico')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')

        medico = get_object_or_404(Medico, id=medico_id)
        Cita.objects.create(medico=medico, fecha=fecha, hora=hora)

        return redirect('lista_citas')

    return render(request, 'citas/lista.html', {'citas': citas, 'medicos': medicos})



def crear_cita(request):
    medicos = Medico.objects.all()

    if request.method == 'POST':
        medico_id = request.POST.get('medico')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')

        medico = get_object_or_404(Medico, id=medico_id)

        # Si tienes pacientes en la base, puedes usar uno aquí
        # paciente = get_object_or_404(Paciente, id=algún_id)

        # Si no usas paciente, asegúrate que el modelo lo permita (null=True, blank=True)
        Cita.objects.create(medico=medico, fecha=fecha, hora=hora)

        return redirect('lista_citas')

    return render(request, 'citas/form.html', {'medicos': medicos})



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
