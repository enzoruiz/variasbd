from django.db import models

# Create your models here.

class Sucursal(models.Model):
	nombre = models.CharField(max_length=45)
	direccion = models.CharField(max_length=45)
	telefono = models.CharField(max_length=45)

	def __str__(self):
		return self.nombre + ' - ' + self.direccion

class Empleado(models.Model):
	nombres = models.CharField(max_length=45)
	apellidos = models.CharField(max_length=45)
	sucursal = models.ForeignKey(Sucursal)