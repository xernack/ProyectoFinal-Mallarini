from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

#############################     CLASS BASED VIEWS (CBV)     ###########################
#from django.views.generic import ListView, CreateView, UpdateView, DetailView
#from django.urls import reverse_lazy
#from django.contrib.auth.mixins import LoginRequiredMixin
#########################################################################################

def home(request):
     
    
    return render(request, "core/index.html")

@login_required
def about(request):
    return render(request, "core/about.html")

def registro_view(request):

    if request.method == "GET":
        return render(request, "core/registro.html", {"form": forms.UserCreationFormulario()})

    else:
        formulario = forms.UserCreationFormulario(request.POST) 
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(request, "core/index.html", {"mensaje": f"Usuario creado: {usuario}"})
        
        else:
            return render(request, "core/registro.html", {"form": formulario})
    
def login_view(request):

    if request.user.is_authenticated:
        return render(request, "core/index.html", {"mensaje": f"Ya estás autenticado en la web cómo: {request.user.username}"})
    
    if request.method == "GET":
        return render(request, "core/login.html", {"form": AuthenticationForm()})
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]
            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)
            return render(request, "core/index.html", {"mensaje": f"Bienvenido {modelo.username}"})
        else:
            return render(request, "core/login.html", {"form": formulario})

def view_logout(request):
    logout(request)
    return render(request,"core/logout.html")    

@login_required
def editar_perfil_view(request):

    usuario = request.user
    avatar = models.Avatar.objects.filter(user=usuario).first()
    avatar_url = avatar.imagen.url if avatar is not None else ""

    if request.method == "GET":
        
        valores_iniciales = {"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name }
        
        
        formulario = forms.UserEditionFormulario(initial=valores_iniciales)
        return render(request, "core/editar-perfil.html", context={"form": formulario, "usuario": usuario, "avatar_url": avatar_url}) 
    
    else:
        formulario = forms.UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.email = informacion["email"]

            usuario.set_password(informacion["password1"])

            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
        return redirect("core:index")
    