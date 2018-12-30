from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from django.conf import settings
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(required = True)
    password = serializers.CharField(style = {'input_type' : 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_email(self, email, password):

        user = None

        if email and password:
            user = authenticate(email = email, password = password)
        else:
            _msg = 'Debes incluir tu email y password'
            raise ValidationError(_msg)
        
        return user
    
    def validate(self, attrs):
       
        email = attrs.get('email', None)
        password = attrs.get('password', None)

        user = None

        
        if email and password:
            user = self._validate_email(email, password)
        
        if user:
            if not user.is_active:
                _msg = 'Cuenta desabilitada'
                raise ValidationError(_msg)

        attrs['user'] = user

        return attrs




            

