from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
   path(r'registration/', include('rest_auth.registration.urls')),
   path(r'', include('rest_auth.urls'))
]
