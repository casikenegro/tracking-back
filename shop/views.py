from django.shortcuts import render
from rest_framework import viewsets, views, mixins, status, permissions, generics
from rest_framework.response import Response
from .models import LinkShop
from .serializers import LinkShopSerializer
from tracking.settings import DEFAULT_IDENTIFIER_SHOP

# Create your views here.

class LinkShopView(generics.ListCreateAPIView,
                   generics.UpdateAPIView,
                   generics.GenericAPIView,
                   views.APIView):

    serializer_class = LinkShopSerializer
    permission_classes = [permissions.IsAdminUser, ]
    

    def list(self, request):
        
        query = LinkShop.objects.all()

        query_longitude = len(query)

        if query_longitude == 1:
            serializer = self.get_serializer(query[query_longitude - 1])
            
            return Response(serializer.data, status = status.HTTP_200_OK)

        return Response("No se ha podido hallar ningun registro en el server", status = status.HTTP_404_NOT_FOUND)

    def create(self, request):
        
        data = request.data

        link = LinkShop.objects.all()
            
        if link.exists():
            return self.update(request, **data)
        
        LinkShop.objects.create(**data)

        message = "Link de tienda actualizado exitosamente"
        
        return Response(message, status = status.HTTP_205_RESET_CONTENT)
    
    def update(self, request, **link):
        
        serializer = self.get_serializer_class()
        
        link_shop = LinkShop.objects.get(key = DEFAULT_IDENTIFIER_SHOP)

        object_to_update = serializer(link_shop, data = link)
        object_to_update.is_valid(raise_exception = True)

        self.perform_update(object_to_update)

        message = "Link actualizado"

        return Response(message, status = status.HTTP_200_OK)
        
        message = "no se pudo actualizar el link de la tienda"

        return Response(message, status = status.HTTP_400_BAD_REQUEST)     
    
                      
    
