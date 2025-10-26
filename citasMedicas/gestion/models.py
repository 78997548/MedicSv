from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"
