from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'inicio'),
    path('nosotros', views.nosotros, name = 'nosotros'),  
    path('productos', views.post_list, name = 'productos'),
    path('login', views.login, name = 'login'),
    path('registro', views.registro, name = 'registro') ,
    path('contactanos', views.contacto, name = 'contactanos'),
    path('listar', views.listar, name = 'listar'),
    path('agregar', views.agregar, name = 'agregar'),
    path('editar/<int:id>', views.modificar, name = 'editar'),
    path('eliminar/<int:id>', views.eliminar, name = 'eliminar'),


    # path('collar', views.collar, name = 'collar') ,
    # path('alimentos', views.alimentos, name = 'alimentos'),
]