from django.shortcuts import render
from .models import Perros, Gatos, Ratas
from .forms import PerrosForm, GatosForm, RatasForm
from django.template import loader

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def agregar_perro(request):
    if request.method == "POST":
        form_perro_info = PerrosForm(request.POST)
        if form_perro_info.is_valid():
            datos = form_perro_info.cleaned_data
            perro_nuevo = Perros(nombre = datos["nombre"], raza = datos["raza"], edad = datos["edad"], tamaño = datos["tamaño"])
            perro_nuevo.save()
            return render(request, "inicio.html", {"mensaje_inicio": "El perrito ha sido agregado, y espera a su nuevo mejor amigo!"})
    else:
        formulario_vacio = PerrosForm()
        return render(request, "agregar_perro.html", {"form_perro":formulario_vacio})

def agregar_gato(request):
    if request.method == "POST":
        form_gato_info = GatosForm(request.POST)
        if form_gato_info.is_valid():
            datos = form_gato_info.cleaned_data
            gato_nuevo = Gatos(nombre = datos["nombre"], raza = datos["raza"], edad = datos["edad"], tamaño = datos["tamaño"])
            gato_nuevo.save()
            return render(request, "inicio.html", {"mensaje_inicio": "El gatito ha sido agregado, y espera a su nuevo mejor amigo!"})
    else:
        formulario_vacio = GatosForm()
        return render(request, "agregar_gato.html", {"form_gato":formulario_vacio})

def agregar_rata(request):
    if request.method == "POST":
        form_rata_info = RatasForm(request.POST)
        if form_rata_info.is_valid():
            datos = form_rata_info.cleaned_data
            rata_nuevo = Ratas(nombre = datos["nombre"], raza = datos["raza"], edad = datos["edad"])
            rata_nuevo.save()
            return render(request, "inicio.html", {"mensaje_inicio": "La ratita ha sido agregada, y espera a su nuevo mejor amigo!"})
    else:
        formulario_vacio = RatasForm()
        return render(request, "agregar_ratas.html", {"form_ratas":formulario_vacio})

def busqueda(request):
    return render(request, "busqueda.html", {"mensaje_busqueda":"Selecciona una raza"})


def resultado_busqueda(request):
    valor_url = request.GET["Raza"]
    if valor_url != "":
        if valor_url != ".":
            razas_filtradas = Perros.objects.filter(raza = valor_url)
        else:
            razas_filtrada = Perros.objects.all()
        return render(request, "resultado_busqueda.html", {"perros_seleccionadas":razas_filtradas})
    else:
        return render(request, "busqueda.html", {"mensaje_busqueda": "Intente nuevamente, valor vacío. "})


