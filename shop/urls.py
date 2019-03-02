from .views import LinkShopView
from django.urls import path, include


urlpatterns = [
    path(r'link_shop', LinkShopView.as_view(), name = 'link_view')
]
