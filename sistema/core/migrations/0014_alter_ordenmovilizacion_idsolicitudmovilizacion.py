# Generated by Django 4.2.6 on 2024-01-19 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_ordenmovilizacion_idsolicitudmovilizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenmovilizacion',
            name='idSolicitudMovilizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.solicitudmovilizacion', verbose_name='Solicitud de Movilización'),
        ),
    ]