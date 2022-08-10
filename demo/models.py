from distutils.command.upload import upload
from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pics')
