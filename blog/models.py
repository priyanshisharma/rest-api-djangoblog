from django.db import models

# Create your models here.

class Post(models.Model):
    #author = models.ForeignKey('auth.User')
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

