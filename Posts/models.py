from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    post_img = models.ImageField(null=True, blank=True, upload_to='post_image')