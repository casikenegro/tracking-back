from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from rest_auth.registration.views import VerifyEmailView
from django.views.generic import TemplateView

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'auth/', include('rest_framework_social_oauth2.urls')),
    path(r'accounts/', include('authentication.urls')),
    path(r'', include('devices.urls')),
    path(r'', include('rest_framework.urls')),
    path(r'', include('shop.urls')),
    path(r'', include('users.urls')),
    path(r'', TemplateView.as_view(template_name = 'index.html'))
]