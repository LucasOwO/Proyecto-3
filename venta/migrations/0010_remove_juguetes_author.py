# Generated by Django 4.1.2 on 2023-06-22 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0009_alter_juguetes_author_alter_juguetes_id_tipo_juguete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juguetes',
            name='author',
        ),
    ]
