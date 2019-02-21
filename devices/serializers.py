from rest_framework import serializers
from .models import Device, Position

class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Device

class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Position