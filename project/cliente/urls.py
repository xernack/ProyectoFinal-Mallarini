
from django.urls import path

from . import views

app_name = "cliente"

urlpatterns = [
    path("", views.home, name = "index"),
    path("crear/", views.crear, name="crearcliente"),
    path("eliminar/<int:id>", views.eliminarcliente, name="eliminar"),
    path("editar/<int:id>", views.editarcliente, name="editar"),
]
