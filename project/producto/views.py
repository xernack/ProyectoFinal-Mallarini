from django.shortcuts import render, redirect

from . import models

def home(request):
    productos = models.Producto.objects.all()
    
    context1 = {"productos": productos}
 
    return render(request, "producto/index.html", context1)

#CREAR PRODUCTOS
def crearproductos(request):
    c1 = models.Categoría(nombre="Limpieza")
    c1.save()
    p1 = models.Producto(nombre="Fabuloso", categoria=c1)
    p1.save()    
    return redirect("producto:index")

def busqueda(request):
    producto_nombre= models.Producto.objects.filter(nombre__contains="agua")
    context= {"producto_nombre":producto_nombre}
    return render(request, "producto/busqueda.html", context)

from . import forms

def crear(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("producto:index")
    else:
        form = forms.ProductoForm()
    return render(request, "producto/crear.html", {"form": form})

def crearc(request):
    if request.method == "POST":
        form = forms.CategoríaForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("producto:index")
    else:
        form = forms.CategoríaForm()
    return render(request, "producto/crearc.html", {"form": form})
       
        
  

    