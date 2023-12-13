from django.shortcuts import render, redirect

from . import models

def home(request):
    clientes = models.Cliente.objects.all()
    context = {"clientes": clientes}

    return render(request, "cliente/index.html", context)

from . import forms

def crear(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cliente = models.Cliente(nombre=data["nombre"], apellido=data["apellido"])
            cliente.save()
            return redirect("cliente:index")
        return render(request, "cliente/crear.html", {"form": form})
    
    else:
        form = forms.ClienteForm()
        return render(request, "cliente/crear.html", {"form": form})
    
def eliminarcliente(request, id):
    
    if request.method == "POST":
        cliente = models.Cliente.objects.get(id=id)
        cliente.delete()
        clientes = models.Cliente.objects.all()
        return render(request, "cliente/index.html", {"clientes": clientes})

def editarcliente(request, id):
    cliente = models.Cliente.objects.get(id=id)

    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            cliente.nombre = data["nombre"]
            cliente.apellido = data["apellido"]
            cliente.save()
            
            return redirect("cliente:index")
        return render(request, "cliente/editar.html", {"form": form})
    
    else:

        form = forms.ClienteForm(initial={
            "nombre": cliente.nombre,
            "apellido": cliente.apellido,
            })
        
        return render(request, "cliente/editar.html", {"form": form, "id": cliente.id})