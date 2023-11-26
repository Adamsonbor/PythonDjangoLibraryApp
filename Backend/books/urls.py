from django.urls import path, include
from rest_framework import routers

from books.views import BookApiView


router = routers.DefaultRouter()
router.register(r'', BookApiView, basename='books')

urlpatterns = [
    path('', include(router.urls)),
]
