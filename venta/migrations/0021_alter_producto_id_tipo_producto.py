# Generated by Django 4.1.2 on 2023-06-23 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0020_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_tipo_producto',
            field=models.ForeignKey(choices=[[1, 'Perro'], [2, 'Gato']], db_column='idTipoProducto', on_delete=django.db.models.deletion.CASCADE, to='venta.tipo_producto'),
        ),
    ]
