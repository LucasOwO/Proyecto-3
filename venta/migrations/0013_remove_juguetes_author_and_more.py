# Generated by Django 4.1.2 on 2023-06-22 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0012_juguetes_id_tipo_juguete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juguetes',
            name='author',
        ),
        migrations.AlterField(
            model_name='juguetes',
            name='id_tipo_juguete',
            field=models.ForeignKey(db_column='idTipoJuguete', default=1, on_delete=django.db.models.deletion.CASCADE, to='venta.tipo_juguete'),
        ),
    ]
