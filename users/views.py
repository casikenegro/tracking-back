from django.shortcuts import render
from rest_framework import viewsets, permissions, generics

from .serializers import userSerializer
from django.contrib.auth.models import User

# Create your views here.

class UsersRolesView(generics.RetrieveAPIView):

    serializer_class = userSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    

    
