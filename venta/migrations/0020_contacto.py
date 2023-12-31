# Generated by Django 4.1.2 on 2023-06-23 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0019_prod_pop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('comentario', models.TextField()),
            ],
        ),
    ]
