# Generated by Django 4.2.6 on 2024-01-19 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_ordencombustible_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudMovilizacion',
            fields=[
                ('idSolicitudMovilizacion', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fechaSolicitud', models.DateField(auto_now=True, verbose_name='Fecha de Solicitud')),
                ('fechaSalida', models.DateField(auto_now=True, verbose_name='Fecha de Salida')),
                ('horaSalida', models.TimeField(verbose_name='Hora de Salida')),
                ('motivo', models.CharField(blank=True, max_length=400, verbose_name='Motivo')),
                ('Ruta', models.CharField(blank=True, max_length=400, verbose_name='Ruta')),
                ('kilometraje', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Kilometraje')),
                ('numeroOcupantes', models.IntegerField(verbose_name='Número de Ocupantes')),
                ('datosOcupantes', models.CharField(max_length=400, verbose_name='Datos de Ocupantes')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Orden de Combustible')),
                ('idPersonal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.personal', verbose_name='Personal')),
                ('idVehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehiculo', verbose_name='Vehículo')),
            ],
            options={
                'verbose_name': 'Solicitud de Movilización',
                'verbose_name_plural': 'Solicitudes de Movilización',
                'db_table': 'solicitudMovilizacion',
                'ordering': ['fechaSolicitud'],
            },
        ),
        migrations.CreateModel(
            name='OrdenMovilizacion',
            fields=[
                ('idOrdenMovilizacion', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fechaSolicitud', models.DateField(auto_now=True, verbose_name='Fecha de Solicitud')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Orden de Combustible')),
                ('idPersonal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.personal', verbose_name='Personal')),
                ('idSolicitudMovilizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehiculo', verbose_name='Vehículo')),
            ],
            options={
                'verbose_name': 'Orden de Movilización',
                'verbose_name_plural': 'Ordenes de Movilización',
                'db_table': 'ordenMovilizacion',
                'ordering': ['fechaSolicitud'],
            },
        ),
    ]
