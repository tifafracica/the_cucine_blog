from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=8)
    email = models.EmailField(unique=True)
    description = models.TextField()
    web_page_link = models.URLField()
    photo = models.URLField()