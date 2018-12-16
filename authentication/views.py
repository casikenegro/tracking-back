from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django_registration.backends.activation.views import ActivationView

# Create your views here.

class ActivationUserView(ActivationView):
    
    def activate(self, *args, **kwargs):
        user = super().activate(args, kwargs)
        
        Token.objects.create(user = user)

        return user


