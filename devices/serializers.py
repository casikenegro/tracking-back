from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Device, Position
from .validators import correctness_struct_serial
import re

class DeviceSerializer(serializers.ModelSerializer):

	serial = serializers.CharField(max_length = 10, validators = [correctness_struct_serial, UniqueValidator(Device.objects.all())])

	date_register = serializers.DateField(format = '%Y/%m/%d')
	
	class Meta:
		fields = ('serial', 'typee', 'date_register', 'user', 'status')
		model = Device

		
class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('device', 'latitude', 'longitude', 'c', 'date_register')
        model = Position

