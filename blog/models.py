from django.db import models
from resdjang import settings

# Create your models here.

class Post(models.Model):
    #author = models.ForeignKey('auth.User')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

