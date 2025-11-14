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
    citas = []  # si no usas base de datos, puedes dejarlo vacío
    medicos = [
        {"id": 1, "nombre": "Dr Wesley Rivera", "especialidad": "Cardiología"},
        {"id": 2, "nombre": "Dr Nestor Alarco", "especialidad": "Ginecología"},
        {"id": 3, "nombre": "Dr Gregorio Casa", "especialidad": "Medico General"},
        {"id": 4, "nombre": "Dr Mario Salazar", "especialidad": "Cardiología"},
        {"id": 5, "nombre": "Dr Meredith Grey", "especialidad": "Neurocirugía"},
        {"id": 6, "nombre": "Dr Glenda Cortez", "especialidad": "Endocrinología"},
        {"id": 7, "nombre": "Dr Juan Blanco", "especialidad": "Medico General"},
    ]
    return render(request, 'citas/lista.html', {'citas': citas, 'medicos': medicos})



def crear_cita(request):
    # Lista estática de médicos
    medicos = [
        {"id": 1, "nombre": "Dr Wesley Rivera", "especialidad": "Cardiología"},
        {"id": 2, "nombre": "Dr Nestor Alarco", "especialidad": "Ginecología"},
        {"id": 3, "nombre": "Dr Gregorio Casa", "especialidad": "Medico General"},
        {"id": 4, "nombre": "Dr Mario Salazar", "especialidad": "Cardiología"},
        {"id": 5, "nombre": "Dr Meredith Grey", "especialidad": "Neurocirugía"},
        {"id": 6, "nombre": "Dr Glenda Cortez", "especialidad": "Endocrinología"},
        {"id": 7, "nombre": "Dr Juan Blanco", "especialidad": "Medico General"},
    ]

    if request.method == 'POST':
        medico_id = request.POST.get('medico')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')

        # Aquí no guardamos en base de datos, solo mostramos como ejemplo
        print(f"Cita creada: Médico {medico_id}, Fecha {fecha}, Hora {hora}")

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
