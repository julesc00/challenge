from django.db import models
from django.contrib.auth.models import User


class Usuarios(models.Model):
    """Create custom user model."""
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True, unique=True)
    saved_password = models.CharField(max_length=100, null=True, blank=True, default="")
    date_created = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """Capitalize name"""
        self.name = self.name.title()

    def __str__(self):
        return self.name
