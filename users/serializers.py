from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ImageUser

class ImageUserSerializer(serializers.ModelSerializer):
    
    def to_representation(self, value):
        if value:
            url = value.image.url
            return '{value.image}'
        return 'null'

    class Meta:
        model = ImageUser
        fields = ('image', )

class userSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):

        try:
            image = obj.imageUrl.image.url
        except Exception:
            image = None


        return {
            'username': obj.username,
            'email' : obj.email,
            'is_superuser' : obj.is_superuser,
            'first_name': obj.first_name,
            'last_name' : obj.last_name,
            'imageUrl' : image
        } 

    class Meta:
        model = User
        fields = ('username', 'email', 'is_superuser', 'imageUrl', 'first_name', 'last_name')