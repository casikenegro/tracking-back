import re
from rest_framework import serializers

def correctness_struct_serial(value):
	regex = '[GMS][0-9]{3}'

	pattern_object = re.compile(regex)

	is_match = pattern_object.match(value)

	if not is_match:
		serializers.ValidationError("El serial del dispositivo no es valido")

