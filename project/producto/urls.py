
from django.urls import path

from . import views

app_name = "producto"

urlpatterns = [
    path("", views.home, name="index"),
    path("crearproductos/", views.crearproductos,),
    path("busqueda/", views.busqueda),
    path("crear/", views.crear, name="creaproducto"),
    path("crearc/", views.crearc, name="creacategoria"),
    path("eliminar/<int:id>", views.eliminarproducto, name="eliminarp"),
    path("editar/<int:id>", views.editarproducto, name ="editar")
]
