# Generated by Django 4.1.2 on 2023-06-22 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0006_tipo_juguete_juguetes_id_tipo_juguete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juguetes',
            name='id_tipo_juguete',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.tipo_juguete'),
        ),
    ]
