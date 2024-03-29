# Generated by Django 4.2.6 on 2023-12-11 21:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canton',
            fields=[
                ('idCanton', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Cantón')),
            ],
            options={
                'verbose_name': 'Cantón',
                'verbose_name_plural': 'Cantónes',
                'db_table': 'canton',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('idCircuito', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10, verbose_name='Código')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Circuito')),
            ],
            options={
                'verbose_name': 'Circuito',
                'verbose_name_plural': 'Circuitos',
                'db_table': 'circuito',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idEstado', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Estado')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'db_table': 'estado',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Marca')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'db_table': 'marca',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('idPais', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Pais')),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Países',
                'db_table': 'pais',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('idPersonal', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('dni', models.CharField(max_length=10, verbose_name='Identificación')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombres')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('tipoSangre', models.CharField(max_length=3, verbose_name='Tipo de Sangre')),
                ('fechaNacimiento', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Nacimiento')),
                ('telefonoCelular', models.CharField(blank=True, max_length=10, verbose_name='Teléfono Celular')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Personal')),
                ('idCanton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.canton', verbose_name='Canton')),
            ],
            options={
                'verbose_name': 'Personal',
                'verbose_name_plural': 'Personales',
                'db_table': 'personal',
                'ordering': ['nombre', 'apellido'],
            },
        ),
        migrations.CreateModel(
            name='Rango',
            fields=[
                ('idRango', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('abreviatura', models.CharField(max_length=10, verbose_name='Abreviatura')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Rango')),
            ],
            options={
                'verbose_name': 'Rango',
                'verbose_name_plural': 'Rangos',
                'db_table': 'rango',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('idRepuesto', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Repuesto')),
            ],
            options={
                'verbose_name': 'Repuesto',
                'verbose_name_plural': 'Repuestos',
                'db_table': 'repuesto',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='SubCiruito',
            fields=[
                ('idSubCiruito', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10, verbose_name='Código')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Sub Circuito')),
                ('idCircuito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.circuito', verbose_name='Circuito')),
            ],
            options={
                'verbose_name': 'Sub Circuito',
                'verbose_name_plural': 'Sub Circuitos',
                'db_table': 'subCircuito',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('idTaller', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
                ('telefono', models.CharField(blank=True, max_length=10, verbose_name='Teléfono')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Taller')),
            ],
            options={
                'verbose_name': 'Taller',
                'verbose_name_plural': 'Talleres',
                'db_table': 'taller',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoPeticion',
            fields=[
                ('idTipoPeticion', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Tipo de Peticion')),
            ],
            options={
                'verbose_name': 'Tipo de Peticion',
                'verbose_name_plural': 'Tipo de Peticiones',
                'db_table': 'tipoPeticion',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoVehiculo',
            fields=[
                ('idTipoVehiculo', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado Tipo de Vehiculo')),
            ],
            options={
                'verbose_name': 'Tipo de Vehiculo',
                'verbose_name_plural': 'Tipos de Vehiculos',
                'db_table': 'tipoVehiculo',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('idVehiculo', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('placa', models.CharField(max_length=20, verbose_name='Placa')),
                ('chasis', models.CharField(max_length=100, verbose_name='Chasis')),
                ('modelo', models.CharField(max_length=200, verbose_name='Modelo')),
                ('motor', models.CharField(max_length=200, verbose_name='Motor')),
                ('kilometraje', models.IntegerField(verbose_name='Kilometraje (km)')),
                ('cilindraje', models.IntegerField(verbose_name='Cilindraje (cc)')),
                ('capacidadCarga', models.IntegerField(verbose_name='Capacidad de Carga (ton)')),
                ('capacidadPasajeros', models.IntegerField(verbose_name='Capacidad de Pasajeros')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Vehiculo')),
                ('idMarca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca', verbose_name='Marca')),
                ('idTipoVehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipovehiculo', verbose_name='Tipo de Vehiculo')),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
                'db_table': 'vehiculo',
                'ordering': ['chasis'],
            },
        ),
        migrations.CreateModel(
            name='VehiculoSubCircuito',
            fields=[
                ('idVehiculoSubCircuito', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fechaInicio', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Inicio')),
                ('fechaFin', models.DateTimeField(blank=True, verbose_name='Fecha de Fin')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Personal Sub Circuito')),
                ('idSubCiruito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subciruito', verbose_name='Sub Circuito')),
                ('idVehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehiculo', verbose_name='Vehículo')),
            ],
            options={
                'verbose_name': 'Vehículo - Sub Circuito',
                'verbose_name_plural': 'Vehículos - Sub Circuitos',
                'db_table': 'vehiculoSubCircuito',
                'ordering': ['idVehiculo__placa'],
            },
        ),
        migrations.CreateModel(
            name='SolicitudMantenimiento',
            fields=[
                ('idSolicitudMantenimiento', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fechaSolicitud', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Solicitud')),
                ('fechaAprobacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de Aprobacion')),
                ('kilometraje', models.IntegerField(verbose_name='Kilometraje (km)')),
                ('observacion', models.TextField(blank=True, verbose_name='Observación')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Solicitud')),
                ('idEstado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado', verbose_name='Estado Aprobacion')),
                ('idPersonal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.personal', verbose_name='Personal')),
                ('idSubCircuito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subciruito', verbose_name='Sub Circuito')),
                ('idVehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehiculo', verbose_name='Vehículo')),
            ],
            options={
                'verbose_name': 'Solicitud de Mantenimiento',
                'verbose_name_plural': 'Solicitudes de Mantenimiento',
                'db_table': 'solicitudMantenimiento',
                'ordering': ['fechaSolicitud'],
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('idProvincia', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Provincia')),
                ('idPais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pais', verbose_name='Pais')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'db_table': 'provincia',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Peticion',
            fields=[
                ('idPeticion', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('detalle', models.TextField(max_length=400, verbose_name='Detalle')),
                ('contacto', models.CharField(max_length=10, verbose_name='Contato')),
                ('apellidos', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('nombres', models.CharField(max_length=200, verbose_name='Nombres')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado Peticion')),
                ('idSubCircuito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subciruito', verbose_name='SubCircuito')),
                ('idTipoPeticion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipopeticion', verbose_name='Tipo de Peticion')),
            ],
            options={
                'verbose_name': 'Peticion',
                'verbose_name_plural': 'Peticiones',
                'db_table': 'Peticion',
                'ordering': ['detalle'],
            },
        ),
        migrations.CreateModel(
            name='PersonalSubCircuito',
            fields=[
                ('idPersonalSubCircuito', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fechaInicio', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Inicio')),
                ('fechaFin', models.DateTimeField(blank=True, verbose_name='Fecha de Fin')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Personal Sub Circuito')),
                ('idPersonal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.personal', verbose_name='Personal')),
                ('idSubCiruito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subciruito', verbose_name='Sub Circuito')),
            ],
            options={
                'verbose_name': 'Personal - Sub Circuito',
                'verbose_name_plural': 'Personales - Sub Circuitos',
                'db_table': 'personalSubCircuito',
                'ordering': ['idPersonal__nombre', 'idPersonal__apellido'],
            },
        ),
        migrations.AddField(
            model_name='personal',
            name='idRango',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rango', verbose_name='Rango'),
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('idParroquia', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Parroquia')),
                ('idCanton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.canton', verbose_name='Canton')),
            ],
            options={
                'verbose_name': 'Parroquia',
                'verbose_name_plural': 'Parroquias',
                'db_table': 'parroquia',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='OrdenMantenimiento',
            fields=[
                ('idOrdenMantenimiento', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fechaOrden', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Orden')),
                ('valorTotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Total')),
                ('observacion', models.TextField(blank=True, verbose_name='Observación')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Orden de Mantenimiento')),
                ('idEstado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado', verbose_name='Estado')),
                ('idSolicitudMantenimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.solicitudmantenimiento', verbose_name='Solicitud de Mantenimiento')),
                ('idTaller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.taller', verbose_name='Taller')),
            ],
            options={
                'verbose_name': 'Orden de Mantenimiento',
                'verbose_name_plural': 'Ordenes de Mantenimiento',
                'db_table': 'ordenMantenimiento',
                'ordering': ['fechaOrden'],
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('idDistrito', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10, verbose_name='Código')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Distrito')),
                ('idParroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.parroquia', verbose_name='Parroquia')),
            ],
            options={
                'verbose_name': 'Distrito',
                'verbose_name_plural': 'Distritos',
                'db_table': 'distrito',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='DetalleOrdenMantenimiento',
            fields=[
                ('idDetalleOrdenMantenimiento', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Detalle de Orden de Mantenimiento')),
                ('idOrdenMantenimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ordenmantenimiento', verbose_name='Orden de Mantenimiento')),
                ('idRepuesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.repuesto', verbose_name='Repuesto')),
            ],
            options={
                'verbose_name': 'Detalle de Orden de Mantenimiento',
                'verbose_name_plural': 'Detalles de Ordenes de Mantenimiento',
                'db_table': 'detalleOrdenMantenimiento',
                'ordering': ['idOrdenMantenimiento__fechaOrden'],
            },
        ),
        migrations.AddField(
            model_name='circuito',
            name='idDistrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.distrito', verbose_name='Distrito'),
        ),
        migrations.AddField(
            model_name='canton',
            name='idProvincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.provincia', verbose_name='Provincia'),
        ),
    ]
