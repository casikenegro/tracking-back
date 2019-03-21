from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Device, Position
from .validators import correctness_struct_serial
import re

class DeviceSerializer(serializers.ModelSerializer):
	
	date_register = serializers.DateTimeField(format = '%m/%d/%Y %H:%M', required = False)

	class Meta:
		fields = ('serial', 'typee', 'date_register', 'user', 'status')
		model = Device

		
class PositionSerializer(serializers.ModelSerializer):

	date_register = serializers.DateTimeField(format = '%m/%d/%Y %H:%M', required = False)

	class Meta:

		fields = ('device', 'latitude', 'longitude', 'c', 'date_register')
		model = Position

