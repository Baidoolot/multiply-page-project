from django.db import models

class Images(models.Model):
    Images = models.ImageField(upload_to='images/')