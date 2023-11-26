from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True, primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    year = models.IntegerField(blank=False,
                               null=False,
                               validators=[MinValueValidator(1)])
