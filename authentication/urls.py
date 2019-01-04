from django.urls import path, include, register_converter, re_path
from django.views.decorators.csrf import csrf_exempt
from rest_auth.registration.views import VerifyEmailView
from allauth.account.views import ConfirmEmailView
from . import converters

register_converter(converters.KeyVerification, 'key_v')

urlpatterns = [
   re_path(r'^account-confirm-email/$', ConfirmEmailView.as_view(), name='account_email_verification_sent'),
   re_path(r'account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(template_name = 'authentication/active.html'), name='account_confirm_email'),
   path(r'registration/', include('rest_auth.registration.urls')),
   path(r'', include('rest_auth.urls')),
]
