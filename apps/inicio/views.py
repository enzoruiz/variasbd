from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Sucursal
from apps.conexion.models import Ruta

# Create your views here.

class InicioView(TemplateView):
	# template_name = "inicio.html"
	def get(self, request, *args, **kwargs):
		sucursal = Sucursal(nombre='Sucursal 1', direccion='Av. Nose', telefono='545454')
		sucursal.save(using='restaurant1')

		sucursal2 = Sucursal(nombre='Sucursal 1', direccion='Av. Nose', telefono='545454')
		sucursal2.save(using='restaurant2')

		sucursales = Sucursal.objects.using('restaurant1').all()
		return render(request, "inicio.html", {"sucursales" : sucursales})

class BienvenidaView(TemplateView):

	def get(self, request, *args, **kwargs):
		user = request.user
		conexion = Ruta.objects.get(usuario_id=user.id)

		sucursal = Sucursal(nombre='Sucursal X', direccion='Av. Nose', telefono='545454')
		sucursal.save(using=str(conexion))

		return render(request, "hola.html", {"conexion" : conexion})

