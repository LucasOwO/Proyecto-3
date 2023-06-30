# from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Producto, Tipo_producto, Prod_pop, Contacto



admin.site.register(Producto)
admin.site.register(Tipo_producto)
admin.site.register(Prod_pop)
admin.site.register(Contacto)

