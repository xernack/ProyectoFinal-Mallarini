from django.shortcuts import render, redirect

from . import models


def home(request):
    productos = models.Producto.objects.all()
    
    context1 = {"productos": productos}
 
    return render(request, "producto/index.html", context1)

#CREAR 
def crearproductos(request):
    c1 = models.Categoría(nombre="Limpieza")
    c1.save()
    p1 = models.Producto(nombre="Fabuloso", categoria=c1)
    p1.save()    
    return redirect("producto:index")

from . import forms

#Busqueda de productos
def busqueda(request):
     

     producto_nombre= models.Producto.objects.filter(nombre__contains="agua")
     context= {"producto_nombre":producto_nombre}
     return render(request, "producto/busqueda.html", context)


#Crear Productos
def crear(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            producto = models.Producto(nombre=data["nombre"], categoria=data["categoria"])
            producto.save()
            return redirect("producto:index")
        return render(request, "producto/crear.html", {"form": form})
    
    else:
        form = forms.ProductoForm()
        return render(request, "producto/crear.html", {"form": form})

#Crear Categorias
def crearc(request):
    if request.method == "POST":
        form = forms.CategoríaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            producto = models.Categoría(nombre=data["nombre"])
            producto.save()
            return redirect("producto:index")
        return render(request, "producto/crearc.html", {"form": form})
    
    else:
        form = forms.CategoríaForm()
        return render(request, "producto/crearc.html", {"form": form})
    

def eliminarproducto(request, id):
    
    if request.method == "POST":
        producto = models.Producto.objects.get(id=id)
        producto.delete()
        productos = models.Producto.objects.all()
        return render(request, "producto/index.html", {"productos": productos})

def editarproducto(request, id):
    producto = models.Producto.objects.get(id=id)

    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            producto.nombre = data["nombre"]
            producto.categoria = data["categoria"]
            producto.save()
            
            return redirect("producto:index")
        return render(request, "producto/editar.html", {"form": form,})
    
    else:

        form = forms.ProductoForm(initial={
            "nombre": producto.nombre,
            "categoria": producto.categoria,
            })
        
        return render(request, "producto/editar.html", {"form": form, "id": producto.id})