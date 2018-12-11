from django.shortcuts import render
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter as GoogleAdapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter as FaceBookAdapter

# Create your views here.

class GoogleAuthentication(SocialLoginView):
	adapter_class = GoogleAdapter

class FaceBookAuthentication(SocialLoginView):
	adapter_class = FaceBookAdapter




