from django.shortcuts import render, redirect

from . import models

def home(request):
    productos = models.Producto.objects.all()
    
    context1 = {"productos": productos}
 
    return render(request, "producto/index.html", context1)


def crearproductos(request):
    c1 = models.Categoría(nombre="Limpieza")
    c2 = models.Categoría(nombre="Cerveza")
    c3= models.Categoría(nombre="Frutas")
    c1.save()
    c2.save()
    c3.save()
    p1 = models.Producto(nombre="Fabuloso", categoria=c1)
    p2 = models.Producto(nombre="Pilsen", categoria=c2)
    p3 = models.Producto(nombre="Manzana", categoria=c3)
    p1.save()    
    p2.save()
    p3.save()
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
       
        
  

    