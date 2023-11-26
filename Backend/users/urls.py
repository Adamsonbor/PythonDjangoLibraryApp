from django.urls import path, include
from rest_framework import routers

from users.views import UserCreationApiView

router = routers.DefaultRouter()
router.register(r'register', UserCreationApiView, basename='user-creation')

urlpatterns = [
        path('', include(router.urls), name='user-creation')
]
