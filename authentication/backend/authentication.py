from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class EmailAuthenticationBackend(ModelBackend):

    def authenticate(self, request, email = None, password = None):

        if email and password:
            try:
                user = User.objects.get(email = email)
        
                if not user.check_password(password):
                    user = None
                    
            except User.DoesNotExist:
                user = None
        
        return user
