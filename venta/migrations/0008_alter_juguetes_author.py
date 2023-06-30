# Generated by Django 4.1.2 on 2023-06-22 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('venta', '0007_alter_juguetes_id_tipo_juguete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juguetes',
            name='author',
            field=models.ForeignKey(db_column='idTipoJuguete', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
