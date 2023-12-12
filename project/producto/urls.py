
from django.urls import path

from . import views

app_name = "producto"

urlpatterns = [
    path("", views.home, name="index"),
    path("crearproductos/", views.crearproductos,),
    path("busqueda/", views.busqueda),
    path("crear/", views.crear),
    path("crearc/", views.crearc)
]
