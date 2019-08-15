from django.db import models


# create a class in models.py
class Job(models.Model):
    image = models.ImageField(upload_to='images/')  # this file is in MEDIA_ROOT
    summary = models.CharField(max_length=200)
