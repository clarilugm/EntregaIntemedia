# Generated by Django 4.1.3 on 2022-12-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMascota', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatos',
            name='tamaño',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='perros',
            name='tamaño',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='ratas',
            name='edad',
            field=models.CharField(max_length=20),
        ),
    ]
