# Generated by Django 4.1.2 on 2023-06-25 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0029_remove_producto_id_producto_id_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.AutoField(db_column='idProducto', primary_key=True, serialize=False),
        ),
    ]
