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
            form.save()
            return redirect("cliente:index")
    else:
        form = forms.ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})