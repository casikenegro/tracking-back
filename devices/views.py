from django.shortcuts import render

# Create your views here.

from .models import Device, Position
from .serializers import DeviceSerializer, PositionSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

class DeviceViewSet(viewsets.ModelViewSet):

    permission_classes = ( IsAuthenticated, )
    serializer_class = DeviceSerializer

    def get_queryset(self):

        if self.request.user.is_superuser:
            return  Device.objects.filter(user = self.request.user)

        return Device.objects.all()

    @action(detail = False, methods = ['get',])
    def positions(self, *args, **kwargs):
        device_positions = Position.objects.filter(device = kwargs.get('serial', ''))
        serializer = PositionSerializer(device_positions)

        




class PositionViewSet(viewsets.ModelViewSet):

    permission_classes = ( IsAuthenticated, )
    serializer_class = PositionSerializer
    
    def get_queryset(self):

        if self.request.user.is_superuser:
            return Position.objects.all()
        
        return Position.objects.filter(user = self.request.user)
    