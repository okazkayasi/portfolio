from django.db import models

# Create a blog model
# title
# pub_date
# body
# image


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    body = models.TextField(blank=True, max_length=16000)
    image = models.ImageField(upload_to='images/')

# Add the Blog app to the settings

# create a migration

# Migrate

# Add to the admin
