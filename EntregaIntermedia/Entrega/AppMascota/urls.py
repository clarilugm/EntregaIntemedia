from django.contrib import admin
from django.urls import path
from AppMascota.views import *
from AppMascota import views
urlpatterns = [
    path("", inicio),
    path("agregarperros/", views.agregar_perro, name= "agregar_perros"),
    path("agregargatos/", views.agregar_gato, name= "agregar_gatos"),
    path("agregarratas/", views.agregar_rata, name= "agregar_ratas"),
    path("busqueda/", views.busqueda, name= "busqueda"),      
    path("resultado_busqueda/", views.resultado_busqueda, name = "resultado_busqueda"),
    path("formulario/", views.formulario, name= "formulario"),
    
]
