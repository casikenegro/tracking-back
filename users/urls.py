from .views import UsersRolesView
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()


urlpatterns = [
    path(r'user/', UsersRolesView.as_view()),
]
