from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.username
