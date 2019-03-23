from .models import Device, Position
from .serializers import DeviceSerializer, PositionSerializer
from rest_framework import viewsets, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView 
import re
from datetime import datetime

def isValidData(data, regex):

    pattern = re.compile(regex)

    match = pattern.search(data)
       
    return match

class DeviceViewSet(viewsets.ModelViewSet):

    permission_classes = ( IsAuthenticated, )
    serializer_class = DeviceSerializer

    lookup_url_kwarg = 'serial'
    lookup_field = 'serial'

    def get_queryset(self):


        user =  self.request.user
            
        if not user.is_superuser:
            return Device.objects.filter(user = user)

        return Device.objects.all()

    def getPartsDataDevice(self, value):

        dict_device = dict(
            serial = value,
            typee = value[0],
            status = 'H',
        )

        return dict_device

    def create(self, request):

        user = request.user
        serial = request.data.get('serial', None)
        
        regex = '([SGM][0-9]{3})'

        match = isValidData(serial, regex)

        if match:
            if not user.is_superuser:
               
                try:
                    device = Device.objects.get(serial = serial)
                    
                    if not device.user:
               
                        device.user = user
                        device.status = 'H'

                        device.save()
                        
                        serializer = DeviceSerializer(device)
                        
                        return Response(serializer.data, status = status.HTTP_200_OK)

                    message = "El dispositivo ya ha sido asignado a otro usuario"

                    return Response(status = status.HTTP_403_FORBIDDEN)

                except Exception as e:

                    message = "El dispositivo no se encuentra registrado para su uso"

                    return Response(message, status = status.HTTP_403_FORBIDDEN)

            parts = self.getPartsDataDevice(match.group(0))
           
            serializer = DeviceSerializer(data = parts)
            
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status = status.HTTP_201_CREATED)
            
        message = 'El dispositivo que ha introducido ya existe'

        return Response(message, status = status.HTTP_400_BAD_REQUEST)



    def isValidRange(self, init, final):
        return init and final
           
    @action(detail = True, methods = ['get'])
    def positions(self, *args, **kwargs):
        

        filter_init = self.request.query_params.get('init', None)
        filter_final = self.request.query_params.get('final', None)
        last = bool(self.request.query_params.get('last', None))
        valid_range = False

        params_to_found = dict(
            device = kwargs.get('serial', '')
        )

        if last:
            params_to_found['last'] = last

        if self.isValidRange(filter_init, filter_final):
            valid_range = True
            params_to_found['init'] = filter_init
            params_to_found['final'] = filter_final

        if params_to_found['device']:
            
            device_positions = Position.positions.getPositionsForRangeDate(**params_to_found, byRange = valid_range)
            
            if device_positions:

                if filter_init and filter_final and not last:
                    serializer = PositionSerializer(device_positions, many = True)
                
                elif not filter_init and not filter_final and last:
                    serializer = PositionSerializer(device_positions)

                else:
                    return Response("Los parametros de consulta no concuerdan")

                return Response(serializer.data)

        message = "No se ha proporcionado un serial valido de dispositivo"

        return Response(message = message, status = status.HTTP_404_NOT_FOUND)



class PositionView(APIView):

    queryset = Position.objects.all()

    def obtainPartsDataPosition(self, values):

        dict_parts = dict(

            serial    =  values[0],
            latitude  =  float(values[1]) + float(values[2]),
            longitude =  float(values[3]) + float(values[4]),
            c         =  float(values[5]) + float(values[6])
        )

        return dict_parts

    def savePositionDevice(self, **kwargs):

        serial = kwargs.get('serial', None)

        device = Device.objects.get(serial = serial)
        
        del kwargs['serial']

        position = Position.objects.create(
            device = device,
            **kwargs
        )
        
        return device


    def get(self, request):

        data = request.query_params.get('data', None)

        if data:

            regex = '([SGM][0-9]{3})([0-9]+[.][0-9]+)-?([0-9]+[.][0-9]+)([0-9]+[.][0-9]+)-?([0-9]+[.][0-9]+)([0-9]+[.][0-9]+)-?([0-9]{4})'

            match = isValidData(data, regex)
            
            if match :
                parts = self.obtainPartsDataPosition(match.groups())

                device = self.savePositionDevice(**parts)

                #if device.user: mandar notificacion al cliente

                return Response(status = status.HTTP_200_OK)

        return Response(status = status.HTTP_400_BAD_REQUEST)


