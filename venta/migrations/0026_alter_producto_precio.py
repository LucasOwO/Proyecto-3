# Generated by Django 4.1.2 on 2023-06-25 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0025_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]