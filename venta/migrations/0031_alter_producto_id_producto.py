# Generated by Django 4.1.2 on 2023-06-25 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0030_alter_producto_id_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
