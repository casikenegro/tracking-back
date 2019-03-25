from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

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

    def getPositionsForRangeDate(self, device, init = None, final = None, last = None, byRange = False):
        
        if byRange: 
            from django.db.models import Q
            from datetime import datetime
            
            inf = datetime.strptime(init, "%d/%m/%Y %H:%M") 
            sup = datetime.strptime(final, "%d/%m/%Y %H:%M")
            
            return self.filter(Q(device =  device) & Q(date_register__gte = inf) & Q(date_register__lte = sup))
        
        devices = self.filter(device = device)

        if not devices.exists():
            return None
            
        if last:
            
            list_devices = list(devices)
            
            last_devices = list_devices[-1]

            return last_devices

        return devices


# Create your models here.

class Device(models.Model):

    serial = models.CharField(verbose_name = 'Serial', max_length = 10, primary_key = True)
    typee = models.CharField(verbose_name = 'Tipo de dispositivo', max_length = 1, choices = type_devices)
    status = models.CharField(verbose_name = 'Estado', max_length = 15, choices = status, default = 'I')
    date_register = models.DateTimeField(verbose_name = 'Fecha de registro', auto_now = True, blank = True)
    user = models.ForeignKey(User, verbose_name = "Usuario", on_delete = models.CASCADE, null = True, blank = True)

class Position(models.Model):

    latitude = models.FloatField(verbose_name = 'Latitud')
    longitude = models.FloatField(verbose_name = 'Longitud')
    c = models.IntegerField(verbose_name = "C")
    date_register = models.DateTimeField(verbose_name = 'Fecha de registro', auto_now_add = True)
    device = models.ForeignKey(Device, verbose_name = "", on_delete  = models.CASCADE, blank = True, null = True)

    objects = models.Manager()
    positions = PositionsRangeDateManager()