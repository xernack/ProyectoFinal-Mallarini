


from django.urls import path

from . import views


app_name = "core"

urlpatterns = [
    path("", views.home, name = "index"),
    path("about/", views.about, name = "about"),
    path("registro/", views.registro_view, name= "registro"),
    path("login/", views.login_view, name= "login"),
    path('logout/', views.view_logout, name='logout'),
]