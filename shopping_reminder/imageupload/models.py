from django.db import models

class UploadImage(models.Model):
    image = models.ImageField('Uploaded image')
    header = models.CharField(max_length=50, default='Shopping Arg')
    description = models.CharField(max_length=50, default='Shopping Notes')