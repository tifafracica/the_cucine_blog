from django.db import models

# Create your models here.
class Profile(models.Model):

    description = models.TextField()
    web_page_link = models.URLField()
    photo = models.URLField()