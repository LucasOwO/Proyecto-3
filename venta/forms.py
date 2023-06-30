from dataclasses import fields 
from django import forms
from django.forms import ModelForm
from .models import Producto, Contacto
from django.contrib.auth.forms import UserCreationForm


class ProductoForm(ModelForm):

    class Meta:
        model=Producto
        # fields = '__all__'
        fields = ["id_producto","titulo", "precio","id_tipo_producto","descripcion","imagen" ]


# class Contactoform(forms.ModelForm):

#     class Meta:
#         model = Contacto
#         fields = '__all__'


class CustomUserCreation(UserCreationForm):
    pass