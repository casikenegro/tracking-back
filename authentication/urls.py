from django.urls import path
from .views import ActivationUserView
from django_registration.backends.activation.views import RegistrationView


urlpatterns = [
    path(r'registration/$', RegistrationView, name = 'registration'),
    path(r'activation/$', ActivationUserView, name = 'activation')
]
