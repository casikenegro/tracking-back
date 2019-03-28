import requests
from users.models import ImageUser
from django.core.files.uploadedfile import SimpleUploadedFile

def associate_image_social_url(strategy, backend, details, response, user = None, *args, **kwargs):
    
    if backend.name == 'google-oauth2':
        
        url = response['image'].get('url') 

        data = requests.get(url)
        data.encoding = 'utf-8'
        
        image_avatar = data.content

        photo = SimpleUploadedFile('avatar.jpg', image_avatar)

        try:
            
            image_user = ImageUser.objects.get(user = user)

            import os

            if os.path.isfile(image_user.image.path):
                os.remove(image_user.image.path)
                
            image_user.image = photo

            image_user.save()

        except Exception:
            
            ImageUser.objects.create(user = user, image = photo)