from .views import UsersRolesViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'users', UsersRolesViewSet)

ListUsersViewSet = UsersRolesViewSet.as_view({
    'get' : 'list'
})

RetrieveUserViewSet = UsersRolesViewSet.as_view({
    'get' : 'retrieve'
})

urlpatterns = [
    path(r'users/', ListUsersViewSet),
    path(r'users/<email>', RetrieveUserViewSet)
]
