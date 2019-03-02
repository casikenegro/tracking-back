from django.db import models
from tracking.settings import DEFAULT_IDENTIFIER_SHOP
# Create your models here.

class LinkShop(models.Model):
    
    key = models.CharField(max_length = 15, verbose_name = 'code', primary_key = True, default = DEFAULT_IDENTIFIER_SHOP)
    link = models.CharField(max_length = 300, verbose_name = 'Enlace', blank = True, null = True)

    class Meta:
        verbose_name = 'Enlace de tienda'
        
