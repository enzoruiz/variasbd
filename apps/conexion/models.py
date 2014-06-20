from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ruta(models.Model):
	usuario = models.OneToOneField(User)
	conexion = models.CharField(max_length=140)

	def __str__(self):
		return self.conexion