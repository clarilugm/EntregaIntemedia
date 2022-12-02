from django import forms

class PerrosForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    tamaño = forms.IntegerField()


class GatosForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    tamaño = forms.IntegerField()


class RatasForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    