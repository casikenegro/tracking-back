from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import userSerializer, ImageUserSerializer
from django.contrib.auth.models import User
from .models import ImageUser
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
import os

# Create your views here.

class UsersRolesView(viewsets.ModelViewSet):

    serializer_class = userSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.request.user
        
        return queryset

    @action(detail = False, methods = ['post',])
    def avatar(self, *args, **kwargs):
        
        user = self.get_queryset()

        data = self.request.data

        try:
            avatar = ImageUser.objects.get(user = user)
            
            if os.path.isfile(avatar.image.path):
                os.remove(avatar.image.path)

            avatar.image = self.request.FILES['avatar']

            avatar.save()

            print("aquiii bienn")
            return Response(status =  status.HTTP_200_OK)
        except Exception:
            print("aqui otro bien")
            ImageUser.objects.create(user = user, image = self.request.FILES['avatar'])

            return Response(status = status.HTTP_201_CREATED)
        
        return Response(status = status.HTTP_400_BAD_REQUEST)

    @avatar.mapping.get
    def avatar_get(self, *args, **kwargs):

        serializer = ImageUserSerializer
        object_serializer = None

        try:
            image = ImageUser.objects.get(user = self.request.user)
            object_serializer = ImageUserSerializer(image)

        except Exception:
            return Response(status = status.HTTP_404_NOT_FOUND)

        return Response(object_serializer.data, status = status.HTTP_200_OK)


    @action(detail = False, methods = ['post',])
    def names(self, *args, **kwargs):

        first = self.request.data.get('first_name', None)
        last = self.request.data.get('last_name', None)

        if first and last:
            user = self.request.user

            user.first_name = first
            user.last_name = last

            user.save()

            return Response(status = status.HTTP_200_OK)
        
        return Response(status = status.HTTP_400_BAD_REQUEST)

    def list(self, *args, **kwargs):

        query = self.get_queryset()

        serializer = self.get_serializer_class()

        serializer_response = serializer(query)

        return Response(serializer_response.data, status = status.HTTP_200_OK)
    

    
