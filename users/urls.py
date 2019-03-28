from .views import UsersRolesView
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash = False)

router.register(r'user', UsersRolesView, basename = 'user')

urlpatterns = [
    path(r'', include(router.urls)),
]
