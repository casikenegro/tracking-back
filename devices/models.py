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

class PositionsRangeDateManager(models.Manager):
    
    def isValidRange(self, init, final):
        return init and final

    def getPositionsForRangeDate(self, device, init = None, final = None, byRange = False):
        
        if byRange: 
            from django.db.models import Q
            from datetime import datetime
            
            inf = datetime.strptime(init, "%Y/%m/%d %H:%m:%s") 
            sup = datetime.strptime(final, "%Y/%m/%d %H:%m:%s")
            
            return self.filter(Q(device =  device) & Q(date_register__gt = inf) & Q(date_register__lte = sup))
        
        return self.filter(device = device)


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

    objects = models.Manager()
    positions = PositionsRangeDateManager()