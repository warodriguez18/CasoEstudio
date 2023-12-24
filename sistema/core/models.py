import datetime
from django.db import models


""" Session """
class Auditoria(models.Model):
    # Campos para usuario de creacion y modificacion
    usuario_creacion = models.CharField(max_length=50, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=50, blank=True, null=True)

    # Campos para fecha de creacion y modificacion
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

""" Base de datos"""
class Pais(Auditoria):
    idPais = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Pais', editable=False)
    

    def __str__(self):
        return self.nombre

    class Meta: 
        db_table = 'pais'
        ordering = ['nombre']
        verbose_name = 'Pais'
        verbose_name_plural = 'Países'


class Provincia(Auditoria):
    idProvincia= models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idPais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name='Pais')
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Provincia', editable=False)

    def __str__(self):
        return self.nombre

    class Meta: 
        db_table = 'provincia'
        ordering = ['nombre']
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'


class Canton(Auditoria):
    idCanton= models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idProvincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name='Provincia')
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Cantón', editable=False)

    def __str__(self):
        return self.nombre

    class Meta: 
        db_table = 'canton'
        ordering = ['nombre']
        verbose_name = 'Cantón'
        verbose_name_plural = 'Cantónes'
    
class Parroquia(Auditoria):
    idParroquia= models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idCanton = models.ForeignKey(Canton, on_delete=models.CASCADE, verbose_name='Canton')
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Parroquia', editable=False)

    def __str__(self):
        return self.nombre

    class Meta: 
        db_table = 'parroquia'
        ordering = ['nombre']
        verbose_name = 'Parroquia'
        verbose_name_plural = 'Parroquias'

class Rango(Auditoria):
    idRango= models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    abreviatura = models.CharField(blank=False, max_length=10, verbose_name='Abreviatura')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Rango', editable=False)

    def __str__(self):
        return self.nombre

    class Meta: 
        db_table = 'rango'
        ordering = ['nombre']
        verbose_name = 'Rango'
        verbose_name_plural = 'Rangos'


class Personal(Auditoria):
    idPersonal = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idCanton = models.ForeignKey(Canton, on_delete=models.CASCADE, verbose_name='Canton')
    idRango = models.ForeignKey(Rango, on_delete=models.CASCADE, verbose_name='Rango')
    dni = models.CharField(blank=False, max_length=10, verbose_name='Identificación')
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombres')
    apellido = models.CharField(blank=False, max_length=200, verbose_name='Apellidos')
    tipoSangre = models.CharField(blank=False, max_length=3, verbose_name='Tipo de Sangre')
    fechaNacimiento = models.DateField(default=datetime.datetime.now, blank=False, verbose_name='Fecha de Nacimiento')
    telefonoCelular = models.CharField(blank=True, max_length=10, verbose_name='Teléfono Celular')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Personal', editable=False)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

    class Meta: 
        db_table = 'personal'
        ordering = [
        'nombre',
        'apellido',
        ]
        verbose_name = 'Personal'
        verbose_name_plural = 'Personales'


class Distrito(Auditoria):
    idDistrito = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idParroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, verbose_name='Parroquia')
    numDistrito = models.IntegerField(blank=False, default=0, verbose_name='No. Distritos')
    codigo = models.CharField(blank=False, max_length=10, verbose_name='Código')
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Distrito', editable=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'distrito'
        ordering = ['nombre']
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'


class Circuito(Auditoria):
    idCircuito = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idDistrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, verbose_name='Distrito')
    numCircuito = models.IntegerField(blank=False, default=0 , verbose_name='No. Circuitos')
    codigo = models.CharField(blank=False, max_length=10, verbose_name='Código')
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Circuito', editable=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'circuito'
        ordering = ['nombre']
        verbose_name = 'Circuito'
        verbose_name_plural = 'Circuitos'

    
class SubCiruito(Auditoria):
    idSubCiruito = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idCircuito = models.ForeignKey(Circuito, on_delete=models.CASCADE, verbose_name='Circuito')
    numSubCircuito = models.IntegerField(blank=False, default=0, verbose_name='No. SubCircuitos')
    codigo = models.CharField(blank=False, max_length=10, verbose_name='Código')
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Sub Circuito', editable=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'subCircuito'
        ordering = ['nombre']
        verbose_name = 'Sub Circuito'
        verbose_name_plural = 'Sub Circuitos'

class PersonalSubCircuito(Auditoria):
    idPersonalSubCircuito = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idPersonal = models.ForeignKey(Personal, on_delete=models.CASCADE, verbose_name='Personal')
    idSubCiruito = models.ForeignKey(SubCiruito, on_delete=models.CASCADE, verbose_name='Sub Circuito')
    fechaInicio = models.DateTimeField(auto_now_add=True, blank=False, verbose_name='Fecha de Inicio')
    fechaFin = models.DateTimeField(blank=True, verbose_name='Fecha de Fin')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Personal Sub Circuito', editable=False)
    
    def __str__(self):
        return self.idSubCiruito.nombre + ': ' + self.idPersonal.nombre + ' ' + self.idPersonal.apellido 
    
    class Meta:
        db_table = 'personalSubCircuito'
        ordering = ['idPersonal__nombre', 'idPersonal__apellido']
        verbose_name = 'Personal - Sub Circuito'
        verbose_name_plural = 'Personales - Sub Circuitos'

class Marca(Auditoria):
    idMarca = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Marca', editable=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'marca'
        ordering = ['nombre']
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

class TipoVehiculo(Auditoria):
    idTipoVehiculo = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado Tipo de Vehiculo', editable=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tipoVehiculo'
        ordering = ['nombre']
        verbose_name = 'Tipo de Vehiculo'
        verbose_name_plural = 'Tipos de Vehiculos'


class Vehiculo(Auditoria):
    idVehiculo = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idMarca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Marca')
    idTipoVehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE, verbose_name='Tipo de Vehiculo')
    placa = models.CharField(blank=False, max_length=20, verbose_name='Placa')
    chasis = models.CharField(blank=False, max_length=100, verbose_name='Chasis')
    modelo = models.CharField(blank=False, max_length=200, verbose_name='Modelo')
    motor = models.CharField(blank=False, max_length=200, verbose_name='Motor')
    kilometraje = models.IntegerField(blank=False, verbose_name='Kilometraje (km)')
    cilindraje = models.IntegerField(blank=False, verbose_name='Cilindraje (cc)')
    capacidadCarga = models.IntegerField(blank=False, verbose_name='Capacidad de Carga (ton)')
    capacidadPasajeros = models.IntegerField(blank=False, verbose_name='Capacidad de Pasajeros')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Vehiculo', editable=False)
    
    def __str__(self):
        return self.idMarca.nombre + ': ' + self.idTipoVehiculo.nombre + ': ' + self.placa
    
    class Meta:
        db_table = 'vehiculo'
        ordering = ['chasis']
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'

class VehiculoSubCircuito(Auditoria):
    idVehiculoSubCircuito = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idVehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name='Vehículo')
    idSubCiruito = models.ForeignKey(SubCiruito, on_delete=models.CASCADE, verbose_name='Sub Circuito')
    fechaInicio = models.DateTimeField(auto_now_add=True, blank=False, verbose_name='Fecha de Inicio')
    fechaFin = models.DateTimeField(blank=True, verbose_name='Fecha de Fin')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Personal Sub Circuito', editable=False)
    
    def __str__(self):
        return self.idSubCiruito.nombre + ': ' + self.idVehiculo.placa
    
    class Meta:
        db_table = 'vehiculoSubCircuito'
        ordering = ['idVehiculo__placa']
        verbose_name = 'Vehículo - Sub Circuito'
        verbose_name_plural = 'Vehículos - Sub Circuitos'

class Estado(Auditoria):
    idEstado = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Estado', editable=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'estado'
        ordering = ['nombre']
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class SolicitudMantenimiento(Auditoria):
    idSolicitudMantenimiento = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idPersonal = models.ForeignKey(Personal, on_delete=models.CASCADE, verbose_name='Personal')
    idVehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name='Vehículo')
    idSubCircuito = models.ForeignKey(SubCiruito, on_delete=models.CASCADE, verbose_name='Sub Circuito')
    idEstado = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name='Estado Aprobacion')
    fechaSolicitud = models.DateTimeField(auto_now_add=True, blank=False, verbose_name='Fecha de Solicitud')
    fechaAprobacion = models.DateTimeField(auto_now=True, blank=False, verbose_name='Fecha de Aprobacion')
    kilometraje = models.IntegerField(blank=False, verbose_name='Kilometraje (km)')
    observacion = models.TextField(blank=True, verbose_name='Observación')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Solicitud', editable=False)

    def __str__(self):
        return self.idSubCircuito.nombre + ': ' + self.idVehiculo.placa
    
    class Meta:
        db_table = 'solicitudMantenimiento'
        ordering = ['fechaSolicitud']
        verbose_name = 'Solicitud de Mantenimiento'
        verbose_name_plural = 'Solicitudes de Mantenimiento'
        

class Repuesto(Auditoria):
    idRepuesto = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    precio = models.DecimalField(blank=False, max_digits=10, decimal_places=2, verbose_name='Precio')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Repuesto', editable=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'repuesto'
        ordering = ['nombre']
        verbose_name = 'Repuesto'
        verbose_name_plural = 'Repuestos'

class Taller(Auditoria):
    idTaller = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    direccion = models.CharField(blank=False, max_length=200, verbose_name='Dirección')
    telefono = models.CharField(blank=True, max_length=10, verbose_name='Teléfono')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Taller', editable=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'taller'
        ordering = ['nombre']
        verbose_name = 'Taller'
        verbose_name_plural = 'Talleres'


class OrdenMantenimiento(Auditoria):
    idOrdenMantenimiento = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idSolicitudMantenimiento = models.ForeignKey(SolicitudMantenimiento, on_delete=models.CASCADE, verbose_name='Solicitud de Mantenimiento')
    idTaller = models.ForeignKey(Taller, on_delete=models.CASCADE, verbose_name='Taller')
    idEstado = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name='Estado')
    fechaOrden = models.DateTimeField(auto_now_add=True, blank=False, verbose_name='Fecha de Orden')
    valorTotal = models.DecimalField(blank=False, max_digits=10, decimal_places=2, verbose_name='Valor Total')
    observacion = models.TextField(blank=True, verbose_name='Observación')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Orden de Mantenimiento', editable=False)

    def __str__(self):
        return self.idSolicitudMantenimiento.idSubCircuito.nombre + ': ' + self.idSolicitudMantenimiento.idVehiculo.placa
    
    class Meta:
        db_table = 'ordenMantenimiento'
        ordering = ['fechaOrden']
        verbose_name = 'Orden de Mantenimiento'
        verbose_name_plural = 'Ordenes de Mantenimiento'

class DetalleOrdenMantenimiento(Auditoria):
    idDetalleOrdenMantenimiento = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idOrdenMantenimiento = models.ForeignKey(OrdenMantenimiento, on_delete=models.CASCADE, verbose_name='Orden de Mantenimiento')
    idRepuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE, verbose_name='Repuesto')
    cantidad = models.IntegerField(blank=False, verbose_name='Cantidad')
    valor = models.DecimalField(blank=False, max_digits=10, decimal_places=2, verbose_name='Valor')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Detalle de Orden de Mantenimiento', editable=False)

    def __str__(self):
        return self.idOrdenMantenimiento.idSolicitudMantenimiento.idSubCircuito.nombre + ': ' + self.idOrdenMantenimiento.idSolicitudMantenimiento.idVehiculo.placa
    
    class Meta:
        db_table = 'detalleOrdenMantenimiento'
        ordering = ['idOrdenMantenimiento__fechaOrden']
        verbose_name = 'Detalle de Orden de Mantenimiento'
        verbose_name_plural = 'Detalles de Ordenes de Mantenimiento'


class TipoPeticion(Auditoria):
    idTipoPeticion = models.BigAutoField(primary_key=True, auto_created=True, unique=True)
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Tipo de Peticion', editable=False)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tipoPeticion'
        ordering = ['nombre']
        verbose_name = 'Tipo de Peticion'
        verbose_name_plural = 'Tipo de Peticiones'

class Peticion(Auditoria):
    idPeticion = models.BigAutoField(primary_key=True, auto_created=True, unique=True)
    idTipoPeticion = models.ForeignKey(TipoPeticion, on_delete=models.CASCADE, verbose_name='Tipo de Peticion')
    idSubCircuito = models.ForeignKey(SubCiruito, on_delete=models.CASCADE, verbose_name='SubCircuito')  
    detalle = models.TextField(blank=False, max_length=400, verbose_name='Detalle')
    contacto = models.CharField(blank=False, max_length=10, verbose_name='Contato')
    apellidos = models.CharField(blank=False, max_length=200, verbose_name='Apellidos')
    nombres = models.CharField(blank=False, max_length=200, verbose_name='Nombres')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado Peticion', editable=False)

    def __str__(self):
        return self.detalle
    
    class Meta:
        db_table = 'Peticion'
        ordering = ['detalle']
        verbose_name = 'Peticion'
        verbose_name_plural = 'Peticiones'

class TipoCombustible(Auditoria):
    idTipoCombustible= models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Tipo Combustible', editable=False)

    def __str__(self):
        return self.nombre

    class Meta: 
        db_table = 'tipoCombustible'
        ordering = ['nombre']
        verbose_name = 'Tipo de Combustible'
        verbose_name_plural = 'Tipos de Combustible'

class Gasolinera(Auditoria):
    idGasolinera= models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    nombre = models.CharField(blank=False, max_length=200, verbose_name='Nombre')
    direccion = models.CharField(blank=False, max_length=400, verbose_name='Dirección')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Gasolinera', editable=False)

    def __str__(self):
        return self.nombre

    class Meta: 
        db_table = 'gasolinera'
        ordering = ['nombre']
        verbose_name = 'Gasolinera'
        verbose_name_plural = 'Gasolineras'


class OrdenCombustible(Auditoria):
    idOrdenCombustible = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idGasolinera = models.ForeignKey(Gasolinera, on_delete=models.CASCADE, verbose_name='Gasolinera')
    idPersonal = models.ForeignKey(Personal, on_delete=models.CASCADE, verbose_name='Personal')
    idVehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name='Vehículo')
    idTipoCombustible = models.ForeignKey(TipoPeticion, on_delete=models.CASCADE, verbose_name='Tipo de Combustible')
    fechaSolicitud = models.DateField(auto_now_add=True, blank=False, verbose_name='Fecha de Solicitud')
    galones = models.DecimalField(blank=False, max_digits=10, decimal_places=2, verbose_name='Galones')
    kilometrajeSalida = models.DecimalField(blank=False, max_digits=10, decimal_places=2, verbose_name='Kilometraje de Salida')
    horaSalida = models.TimeField(blank=False, verbose_name='Hora de Salida')
    horaLlegada = models.TimeField(blank=False, verbose_name='Hora de Salida')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Orden de Combustible', editable=False)

    def __str__(self):
        return self.fechaSolicitud

    class Meta: 
        db_table = 'ordenCombustible'
        ordering = ['fechaSolicitud']
        verbose_name = 'Orden de Combustible'
        verbose_name_plural = 'Ordenes de Combustible'

class DespachoCombustible(Auditoria):
    idDespachoCombustible = models.BigAutoField(auto_created=True, primary_key=True, unique=True)
    idOrdenCombustible = models.ForeignKey(OrdenCombustible, on_delete=models.CASCADE, verbose_name='Ordne de Combustible')
    fechaOrden = models.DateTimeField(blank=False, verbose_name='Fecha de Despacho')
    galones = models.DecimalField(blank=False, max_digits=10, decimal_places=2, verbose_name='Galones')
    estado = models.BooleanField(blank=False, default=True, verbose_name='Estado de Despacho de Combustible', editable=False)

    def __str__(self):
        return self.fechaOrden

    class Meta: 
        db_table = 'despachoCombustible'
        ordering = ['fechaOrden']
        verbose_name = 'Despacho de Combustible'
        verbose_name_plural = 'Despachos de Combustible'