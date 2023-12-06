from django.db import models

class Cliente(models.Model):
   nombre = models.CharField(max_length=100) 
   apellido = models.CharField(max_length=100) 

   
   def __str__(self):
    return f"{self.nombre} {self.apellido}"