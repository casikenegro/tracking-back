from rest_framework import routers
from .views import DeviceViewSet, PositionViewSet
from django.urls import path, include


router =  routers.SimpleRouter()

router.register(r'devices', DeviceViewSet, basename = 'device')

urlpatterns = [
    path(r'', include(router.urls))
]

