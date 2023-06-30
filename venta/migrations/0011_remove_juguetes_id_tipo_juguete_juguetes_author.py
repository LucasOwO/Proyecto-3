# Generated by Django 4.1.2 on 2023-06-22 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('venta', '0010_remove_juguetes_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juguetes',
            name='id_tipo_juguete',
        ),
        migrations.AddField(
            model_name='juguetes',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]