from django.db import models

class User(models.Model):
    class Meta:
        # Username and email must be unique set
        # but email should not be unique
        unique_together = ('username', 'email')

    username = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.username
