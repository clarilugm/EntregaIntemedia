# Generated by Django 4.1.3 on 2022-12-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMascota', '0002_alter_gatos_tamaño_alter_perros_tamaño_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('tamaño', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='ratas',
            name='tamaño',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]
