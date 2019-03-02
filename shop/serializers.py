from rest_framework import serializers
from .models import LinkShop
from tracking.settings import DEFAULT_IDENTIFIER_SHOP

class LinkShopSerializer(serializers.ModelSerializer):
                
    class Meta:
        model = LinkShop
        fields = '__all__'
        