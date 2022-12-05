from django.shortcuts import render
from .models import Perros, Gatos, Ratas
from .forms import PerrosForm, GatosForm, RatasForm
from .forms import formulario
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "AppMascota/inicio.html")

def agregar_perro(request):
    if request.method == "POST":
        form_perro_info = PerrosForm(request.POST)
        if form_perro_info.is_valid():
            datos = form_perro_info.cleaned_data
            perro_nuevo = Perros(nombre = datos["nombre"], raza = datos["raza"], edad = datos["edad"], tamaño = datos["tamaño"])
            perro_nuevo.save()
            return render(request, "AppMascota/inicio.html", {"mensaje_inicio": "El perrito ha sido agregado, y espera a su nuevo mejor amigo!"})
    else:
        formulario = PerrosForm()
        return render(request, "AppMascota/agregar_perro.html", {"form_perro":formulario})

def agregar_gato(request):
    if request.method == "POST":
        form_gato_info = GatosForm(request.POST)
        if form_gato_info.is_valid():
            datos = form_gato_info.cleaned_data
            gato_nuevo = Gatos(nombre = datos["nombre"], raza = datos["raza"], edad = datos["edad"], tamaño = datos["tamaño"])
            gato_nuevo.save()
            return render(request, "inicio.html", {"mensaje_inicio": "El gatito ha sido agregado, y espera a su nuevo mejor amigo!"})
    else:
        formulario = GatosForm()
        return render(request, "AppMascota/agregar_gato.html", {"form_gato":formulario})

def agregar_rata(request):
    if request.method == "POST":
        form_rata_info = RatasForm(request.POST)
        if form_rata_info.is_valid():
            datos = form_rata_info.cleaned_data
            rata_nuevo = Ratas(nombre = datos["nombre"], raza = datos["raza"], edad = datos["edad"], tamaño = datos["tamaño"])
            rata_nuevo.save()
            return render(request, "AppMascota/inicio.html", {"mensaje_inicio": "La ratita ha sido agregada, y espera a su nuevo mejor amigo!"})
    else:
        formulario = RatasForm()
        return render(request, "AppMascota/agregar_rata.html", {"form_ratas":formulario})



def busqueda(request):
    return render(request, "AppMascota/busqueda.html", {"mensaje_busqueda":"Selecciona una raza"})


def resultado_busqueda(request):
    if request.GET["raza"]:
        raza=request.GET["raza"]
        busqueda = Perros.objects.filter(raza__icontains=raza)  
        return render(request, "resultado_busqueda.html", {'busqueda': busqueda })
    else:
        return render(request, "busqueda.html")


def formulario(request):

    if request.method=="POST":
        form=PerrosForm(request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            print(datos)
            nombre=datos["nombre"]
            raza=datos["raza"]
            edad=datos["edad"]
            tamaño=datos["tamaño"]
            formulario= Perros(nombre=nombre, raza=raza, edad=edad, tamaño=tamaño)
            formulario.save()
            return render (request, "AppMascota/formulario.html", {"mensaje": "El perrito fue agregado correctamente:) <3"})
    else:
        formulario=PerrosForm()
    return render (request,"AppMascota/formulario.html", {"formulario": formulario})


