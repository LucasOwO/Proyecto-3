# Generated by Django 4.1.2 on 2023-06-22 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('venta', '0008_alter_juguetes_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juguetes',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='juguetes',
            name='id_tipo_juguete',
            field=models.ForeignKey(db_column='idTipoJuguete', on_delete=django.db.models.deletion.CASCADE, to='venta.tipo_juguete'),
        ),
    ]
