from django.urls import path
from . import views

urlpatterns = [
    
    # Home / Login
    path('', views.login_view, name='login'),
 
    
    #Registro
    path('registro/',views.register_view, name='registro'),
    
    
    # Menu
    path('menu/', views.menu_view, name='menu'),
    
    #logout
    path('logout/', views.logout_view, name='logout'),
    
    
    # Pacientes
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/nuevo/', views.crear_paciente, name='crear_paciente'),
    path('pacientes/editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:id>/', views.eliminar_paciente, name='eliminar_paciente'),

    # Médicos
    path('medicos/', views.lista_medicos, name='lista_medicos'),
    path('medicos/nuevo/', views.crear_medico, name='crear_medico'),
    path('medicos/editar/<int:id>/', views.editar_medico, name='editar_medico'),
    path('medicos/eliminar/<int:id>/', views.eliminar_medico, name='eliminar_medico'),

    # Citas
    path('citas/', views.lista_citas, name='lista_citas'),
    path('citas/nuevo/', views.crear_cita, name='crear_cita'),
    path('citas/editar/<int:id>/', views.editar_cita, name='editar_cita'),
    path('citas/eliminar/<int:id>/', views.eliminar_cita, name='eliminar_cita'),
]
