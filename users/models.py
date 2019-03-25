from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

def upload_image_avatar(instance, filename):
    return '{}/{}'.format(instance.user.email, filename)

class ImageUser(models.Model):

    user = models.OneToOneField(User, verbose_name = "Usuario", on_delete = models.CASCADE)

    image = models.ImageField(verbose_name = 'Imagen de perfil',
        upload_to = upload_image_avatar,
        blank=True,
        null=True)