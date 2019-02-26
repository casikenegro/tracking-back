from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Device, Position
from .validators import correctness_struct_serial
import re

class DeviceSerializer(serializers.ModelSerializer):

	serial = serializers.CharField(max_length = 10, validators = [correctness_struct_serial, UniqueValidator(Device.objects.all())])

	class Meta:
		fields = ('serial', 'typee', 'date_register', 'user')
		model = Device

		return Device(serial = serial_device, typee = type_device )

class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Position

