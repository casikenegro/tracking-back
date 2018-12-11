from django.urls import path, include
from . import views

extrapatterns = [
	path(r'login/google/', views.GoogleAuthentication.as_view(), name = 'google'),
	path(r'login/facebook/', views.FaceBookAuthentication.as_view(), name = 'facebook'),
	path(r'', include('rest_framework_social_oauth2.urls', namespace = 'social_oauth2'))
]

urlpatterns = [
	path('account/',  include(extrapatterns)),
]