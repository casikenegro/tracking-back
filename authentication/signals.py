from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
from allauth.account.models import EmailAddress
from django.shortcuts import get_object_or_404

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_token_signal(sender, instance = None, created = False, **kwargs):
    if created:
        if instance.is_superuser:
                email = EmailAddress(user = instance, verified = True, email = instance.email, primary = True)
                email.save()

        Token.objects.create(user = instance)