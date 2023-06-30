# from django.db import models

# Create your models here.


from django.conf import settings
from django.db import models
from django.utils import timezone





opciones_tipo = [
    [1, "Perro"],
    [2, "Gato"]
]


    
class Tipo_producto(models.Model):
    id_tipo_producto = models.AutoField(db_column='idTipoProducto', primary_key=True,default=0)
    tipo_producto = models.CharField(max_length=20, blank=False, null=False)
        
    def __str__(self):
        return str(self.tipo_producto)



class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.IntegerField( null=True)
    id_tipo_producto = models.ForeignKey("Tipo_producto" ,on_delete=models.CASCADE, db_column='idTipoProducto') 
    imagen           = models.ImageField(upload_to="imagenes/producto", null=True)
    

    def __str__(self):
        return self.titulo
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()




class Prod_pop(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.IntegerField( null=True)
    id_tipo_producto = models.ForeignKey("Tipo_producto", on_delete=models.CASCADE, db_column='idTipoProducto') 
    imagen           = models.ImageField(upload_to="imagenes/prod_pop", null=True)
    

    def __str__(self):
        return self.titulo
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        
    



class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.IntegerField()
    comentario = models.TextField()
    
    
    def __str__(self):
        return self.nombre




# class Genero(models.Model):

#     id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
#     genero     = models.CharField(max_length=20, blank=False, null=False)
#     def __str__(self):

#         return str(self.genero)
 