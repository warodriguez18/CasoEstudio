# Generated by Django 4.2.6 on 2024-01-19 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_solicitudmovilizacion_fechasalida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenmovilizacion',
            name='idEstado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.estado', verbose_name='Estado'),
            preserve_default=False,
        ),
    ]