from django.urls import path, include, register_converter, re_path
from django.views.decorators.csrf import csrf_exempt
from rest_auth.registration.views import VerifyEmailView
from rest_auth.views import (PasswordResetView, PasswordResetConfirmView)
from allauth.account.views import ConfirmEmailView

urlpatterns = [
   re_path(r'^account-confirm-email/$', ConfirmEmailView.as_view(), name='account_email_verification_sent'),
   re_path(r'account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(template_name = 'authentication/active.html'), name='account_confirm_email'),
   path(r'registration/', include('rest_auth.registration.urls')),
   path(r'password/reset/', PasswordResetView.as_view()),
   path(r'password/reset/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
   path(r'', include('rest_auth.urls')),
]
