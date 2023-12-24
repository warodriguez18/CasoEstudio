# Generated by Django 4.2.6 on 2023-12-24 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_circuito_numcircuito_distrito_numdistrito_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gasolinera',
            fields=[
                ('idGasolinera', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=400, verbose_name='Dirección')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Gasolinera')),
            ],
            options={
                'verbose_name': 'Gasolinera',
                'verbose_name_plural': 'Gasolineras',
                'db_table': 'gasolinera',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoCombustible',
            fields=[
                ('idTipoCombustible', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Tipo Combustible')),
            ],
            options={
                'verbose_name': 'Tipos de Combustible',
                'verbose_name_plural': 'Tipos de Combustible',
                'db_table': 'tipoCombustible',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='OrdenCombustible',
            fields=[
                ('idOrdenCombustible', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fechaSolicitud', models.DateField(auto_now_add=True, verbose_name='Fecha de Solicitud')),
                ('galones', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Galones')),
                ('kilometrajeSalida', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Kilometraje de Salida')),
                ('horaSalida', models.TimeField(verbose_name='Hora de Salida')),
                ('horaLlegada', models.TimeField(verbose_name='Hora de Salida')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Orden de Combustible')),
                ('idGasolinera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.gasolinera', verbose_name='Gasolinera')),
                ('idPersonal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.personal', verbose_name='Personal')),
                ('idTipoCombustible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipopeticion', verbose_name='Tipo de Combustible')),
                ('idVehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehiculo', verbose_name='Vehículo')),
            ],
            options={
                'verbose_name': 'Orden de Combustible',
                'verbose_name_plural': 'Ordenes de Combustible',
                'db_table': 'ordenCombustible',
                'ordering': ['fechaSolicitud'],
            },
        ),
        migrations.CreateModel(
            name='DespachoCombustible',
            fields=[
                ('idDespachoCombustible', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('usuario_modificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fechaOrden', models.DateTimeField(verbose_name='Fecha de Despacho')),
                ('galones', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Galones')),
                ('estado', models.BooleanField(default=True, editable=False, verbose_name='Estado de Despacho de Combustible')),
                ('idOrdenCombustible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ordencombustible', verbose_name='Ordne de Combustible')),
            ],
            options={
                'verbose_name': 'Despacho de Combustible',
                'verbose_name_plural': 'Despachos de Combustible',
                'db_table': 'despachoCombustible',
                'ordering': ['fechaOrden'],
            },
        ),
    ]
