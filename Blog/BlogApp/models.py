from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class BlogPost(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.TextField(blank=True, max_length=255)
    body = models.TextField(blank=True, max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

