from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    def validate_isbn(self, value):
        if self.instance and self.instance.isbn != value:
            raise ValidationError("You may not edit isbn!")
        return value
    
    class Meta:
        model = Book
        fields = '__all__'
