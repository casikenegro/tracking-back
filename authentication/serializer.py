from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):

        user = User.objects.create(**validated_data)

        return user