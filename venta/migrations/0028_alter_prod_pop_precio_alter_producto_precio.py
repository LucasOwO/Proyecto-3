# Generated by Django 4.1.2 on 2023-06-25 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0027_rename_text_prod_pop_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prod_pop',
            name='precio',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(null=True),
        ),
    ]
