import requests
from users.models import ImageUser

def associate_image_social_url(strategy, backend, details, response, user = None, *args, **kwargs):
    
    if backend.name == 'google-oauth2':
        
        url = response['image'].get('url') 
        print(url)

        image_avatar = requests.get(url).content

        try:
        
             image_user = ImageUser.objects.get(user = user)

             image_user.image = image_avatar

             image_user.save()

        except Exception:
             ImageUser.objects.create(user = user, image = image_avatar)