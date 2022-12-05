from django.db import models

# Create your models here.
class Perros(models.Model):
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    edad = models.IntegerField()
    tamaño = models.CharField(max_length=20)


class Gatos(models.Model):
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    edad = models.IntegerField()
    tamaño = models.CharField(max_length=20)



class Ratas(models.Model):
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    edad = models.CharField(max_length=20)
    tamaño = models.CharField(max_length=20)
    
    
class formulario(models.Model):
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    edad = models.IntegerField()
    tamaño = models.CharField(max_length=20)





