# Generated by Django 4.1.2 on 2023-06-22 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0017_producto_tipo_producto_delete_juguetes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alimentos',
            name='author',
        ),
        migrations.RemoveField(
            model_name='collares',
            name='author',
        ),
        migrations.DeleteModel(
            name='Tipo_alimento',
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/producto'),
        ),
        migrations.DeleteModel(
            name='Alimentos',
        ),
        migrations.DeleteModel(
            name='Collares',
        ),
    ]
