from django.db import models

class Categoría(models.Model):
    nombre = models.CharField(max_length=100) 
 
    def __str__(self):
       return self.nombre  
 


class Producto(models.Model):
    nombre = models.CharField(max_length=100) 
    categoria = models.ForeignKey(Categoría, on_delete=models.SET_NULL, null=True, blank=True)
     
    def __str__(self):
     return f"{self.nombre} {self.categoria}"


 

