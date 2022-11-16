from django.db import models

# Create your models here.
class Message(models.Model):

    user = models.CharField(max_length=20)
    message = models.TextField()