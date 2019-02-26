from django.db import models
from django.contrib.auth.models import User

type_devices = (
    ('G', 'Seguimiento'),
    ('S', 'Valor en mapa'),
    ('M', 'Valor en modulo'),
)

status = (
    ('H' , 'Habilitado'),
    ('I', 'Inabilitado'),
)


# Create your models here.

class Device(models.Model):
    
    serial = models.CharField(verbose_name = 'Serial', max_length = 10, primary_key = True, validators = [])
    typee = models.CharField(verbose_name = 'Tipo de dispositivo', max_length = 1, choices = type_devices)
    status = models.CharField(verbose_name = 'Estado', max_length = 15, choices = status, default = 'I')
    date_register = models.DateField(verbose_name = 'Fecha de registro', auto_now_add =  True)
    user = models.ForeignKey(User, verbose_name = "Usuario", on_delete = models.CASCADE, null = True, blank = True)

class Position(models.Model):

    latitude = models.FloatField(verbose_name = 'Latitud')
    longitude = models.FloatField(verbose_name = 'Longitud')
    c = models.IntegerField(verbose_name = "C")
    date_register = models.DateField(verbose_name = 'Fecha de registro', auto_now_add = True)
    device = models.ForeignKey(Device, verbose_name = "", on_delete  = models.CASCADE, blank = True, null = True)
