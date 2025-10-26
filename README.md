# Proyecto MedicSv

## Semana 3 – Implementación del CRUD en Django

### Tema general
Durante esta semana trabajé en la creación de las vistas, formularios y plantillas para las entidades principales del sistema: Paciente, Médico y Cita, utilizando Django y Bootstrap.

### Objetivo
Desarrollar las operaciones básicas del CRUD (crear, ver, editar y eliminar) aplicando el patrón Modelo–Vista–Template (MVT) en Django.

### Descripción del proyecto
MedicSv es una aplicación sencilla hecha con Django que sirve para administrar pacientes, médicos y citas.  
Cada módulo permite:
- Agregar nuevos registros
- Ver la lista de datos
- Editar información
- Eliminar registros

Todo el diseño se realizó con Bootstrap para que las páginas se vean más ordenadas y modernas.


### Modelos usados
- Paciente: nombre, edad, dirección  
- Médico: nombre, especialidad  
- Cita: paciente, médico, fecha, hora  

Cada modelo tiene su propio formulario y vistas CRUD completas.

### Funciones principales
- Listar todos los registros
- Crear nuevos datos
- Editar información existente
- Eliminar registros con confirmación
- Validar los formularios antes de guardar

### Diseño
El proyecto usa Bootstrap 5.3 para los botones, tablas y formularios.  
Las plantillas están conectadas a un archivo base (base.html) que sirve como plantilla principal para todo el sistema.

### Cómo ejecutar el proyecto
1. Abrir la carpeta del proyecto en Visual Studio Code  
2. En la terminal ejecutar:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

3. Entrar al navegador en:
- Panel admin: http://127.0.0.1:8000/admin/
- Pacientes: http://127.0.0.1:8000/pacientes/
- Médicos: http://127.0.0.1:8000/medicos/
- Citas: http://127.0.0.1:8000/citas/

### Reflexión personal
Este proyecto me ayudó bastante a entender cómo se conecta todo dentro de Django.  
Al principio me costó con las rutas y los templates, pero poco a poco fui comprendiendo el patrón MVT.  
Aprendí cómo Bootstrap mejora el diseño y cómo el CRUD permite manejar los datos desde el navegador.  
Fue una buena práctica para seguir aprendiendo desarrollo web.

### Tecnologías usadas
- Python 3  
- Django 5  
- SQLite  
- Bootstrap 5  
- Visual Studio Code

### Repositorio
En este repositorio se incluyen todos los archivos actualizados del proyecto, con los modelos, formularios, vistas y plantillas HTML.



