from .models import Device, Position
from .serializers import DeviceSerializer, PositionSerializer
from rest_framework import viewsets, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView 
import re


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
            typee = value[0]
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

                        return Response(status = status.HTTP_200_OK)

                    message = "El dispositivo ya ha sido asignado a otro usuario"

                    return Response(status = status.HTTP_403_FORBIDDEN)

                except Exception as e:

                    message = "El dispositivo no se encuentra registrado para su uso"

                    return Response(message, status = status.HTTP_403_FORBIDDEN)

            parts = self.getPartsDataDevice(match.group(0))

            serializer = DeviceSerializer(data = parts)

            if serializer.is_valid():

                serializer.save()

                return Response(status = status.HTTP_201_CREATED)

            message = 'El dispositivo que ha introducido ya existe'

            return Response(message, status = status.HTTP_400_BAD_REQUEST)



    def isValidRange(self, init, final):
        return init and final
           
    @action(detail = True, methods = ['get'])
    def positions(self, *args, **kwargs):
        

        filter_init = self.request.query_params.get('init', None)
        filter_final = self.request.query_params.get('final', None)

        valid_range = False

        params_to_found = dict(
            device = kwargs.get('serial', '')
        )

        if self.isValidRange(filter_init, filter_final):
            valid_range = True
            params_to_found['init'] = filter_init
            params_to_found['final'] = filter_final

        if params_to_found['device']:
            device_positions = Position.positions.getPositionsForRangeDate(**params_to_found, byRange = valid_range)
            serializer = PositionSerializer(device_positions, many = True)

            return Response(serializer.data)

        message = "No se ha proporcionado un serial valido de dispositivo"

        return Response(message = message, status = status.HTTP_404_NOT_FOUND)



class PositionView(APIView):

    queryset = Position.objects.all()

    def obtainPartsDataPosition(self, values):


        dict_parts = dict(

            serial    =  values[0],
            latitude  =  values[1],
            longitude =  values[2],
            c         =  values[3]
        )

        return dict_parts

    def savePositionDevice(self, **kwargs):

        serial = kwargs.get('serial', None)

        device = Device.objects.get(serial = serial)

        latitude = kwargs.get('latitude', None)
        longitude = kwargs.get('longitude', None)
        c = kwargs.get('c', None)

        position = Position.objects.create(
            device = device,
            latitude = latitude.split('-')[1],
            longitude = longitude.split('-')[1],
            c = c.split('-')[1]
        )

        return device


    def get(self, request):

        data = request.query_params.get('data', None)

        if data:

            regex = '([SGM][0-9]{3})(A-?[0-9]+[.][0-9]+)(B-?[0-9]+[.][0-9]+)(C-?[0-9]+)'

            match = isValidData(data, regex)
            
            if match :
                parts = self.obtainPartsDataPosition(match.groups())

                device = self.savePositionDevice(**parts)

                #if device.user: mandar notificacion al cliente

                return Response(status = status.HTTP_200_OK)

        return Response(status = status.HTTP_400_BAD_REQUEST)


