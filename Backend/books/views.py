from rest_framework import viewsets

from books.models import Book
from books.serializers import BookSerializer


# Book API Viewset for CRUD operations
class BookApiView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
