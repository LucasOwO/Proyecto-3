# Generated by Django 4.1.2 on 2023-06-25 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0028_alter_prod_pop_precio_alter_producto_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id',
        ),
        migrations.AddField(
            model_name='producto',
            name='id_producto',
            field=models.AutoField(db_column='idProducto', default=0, primary_key=True, serialize=False),
        ),
    ]
