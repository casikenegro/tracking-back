from django.shortcuts import render
from allauth.account.views import ConfirmEmailView
from django.views.generic import View
# Create your views here.

class VerifyEmailView(View):

    def get(self, *args, **kwargs):
        print("holaaaaaaa")
        
        #super(ConfirmEmailView, self).get(*args, **kwargs)

