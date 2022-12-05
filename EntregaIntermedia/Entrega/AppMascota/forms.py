from django import forms

class PerrosForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    tamaño = forms.CharField(max_length=20)


class GatosForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    tamaño = forms.CharField(max_length=20)

class RatasForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    edad = forms.CharField(max_length=20)
    
class formulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    tamaño = forms.CharField(max_length=20)

