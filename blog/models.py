from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    body = models. TextField()

    def __str__(self):
        return self.title