from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Device, Position
from .validators import correctness_struct_serial
import re

class DeviceSerializer(serializers.ModelSerializer):
	
	date_register = serializers.DateTimeField(format = '%d/%m/%Y %H:%M', required = False)

	def to_representation(self, obj):

		try:
			user = obj.user.first_name + obj.user.last_name
		except Exception:
			user = None

		try:
			date = obj.date_register.strftime(' %d/%m/%Y %H:%M')
		except Exception:
			date = None

		return {
			'serial' : obj.serial,
			'typee' : obj.typee,
			'date_register' : date,
			'status' : obj.status,
			'user' : user
		}

	class Meta:
		fields = ('serial', 'typee', 'date_register', 'user', 'status', 'first_name', 'last_name')
		model = Device

		
class PositionSerializer(serializers.ModelSerializer):

	date_register = serializers.DateTimeField(format = '%d/%m/%Y %H:%M', required = False)

	class Meta:

		fields = ('device', 'latitude', 'longitude', 'c', 'date_register')
		model = Position

