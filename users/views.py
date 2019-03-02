from django.shortcuts import render
from rest_framework import viewsets, permissions

from .serializers import userSerializer
from django.contrib.auth.models import User

# Create your views here.

class UsersRolesViewSet(viewsets.ModelViewSet):

    serializer_class = userSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    lookup_url_kwarg = 'email'
    lookup_field = 'email'