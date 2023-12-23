from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Personal)
admin.site.register(models.Vehiculo)
admin.site.register(models.Pais)
admin.site.register(models.Provincia)
admin.site.register(models.Canton)
admin.site.register(models.Distrito)
admin.site.register(models.Circuito)
admin.site.register(models.SubCiruito)
admin.site.register(models.Marca)
admin.site.register(models.PersonalSubCircuito)
admin.site.register(models.Parroquia)
admin.site.register(models.VehiculoSubCircuito)
admin.site.register(models.TipoVehiculo)
admin.site.register(models.Rango)
admin.site.register(models.Estado)
admin.site.register(models.SolicitudMantenimiento)
admin.site.register(models.Repuesto)
admin.site.register(models.Taller)
admin.site.register(models.OrdenMantenimiento)
admin.site.register(models.DetalleOrdenMantenimiento)
