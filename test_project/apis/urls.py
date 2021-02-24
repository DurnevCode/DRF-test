
from django.urls import include, path
from rest_framework import routers

from .views import *
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
router.register(r'geeks', GeeksModelViewSet, basename='GeeksModel')

# app_name will help us do a reverse look-up latter.



urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]