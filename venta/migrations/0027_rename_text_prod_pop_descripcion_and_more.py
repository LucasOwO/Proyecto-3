# Generated by Django 4.1.2 on 2023-06-25 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0026_alter_producto_precio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prod_pop',
            old_name='text',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='prod_pop',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RemoveField(
            model_name='prod_pop',
            name='author',
        ),
        migrations.AlterField(
            model_name='prod_pop',
            name='precio',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]
