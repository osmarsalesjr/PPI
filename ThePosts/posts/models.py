from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    data_published = models.DateTimeField(auto_now_add=True)
    data_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
