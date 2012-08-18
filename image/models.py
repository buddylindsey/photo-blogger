from django.db import models

class Image(models.Model):
    location = models.CharField(max_length=200)
    description = models.TextField()
    expiration = models.DateTimeField(blank=True,null=True)
    latitude = models.DecimalField(max_digits=13, decimal_places=7,blank=True,null=True)
    longitude = models.DecimalField(max_digits=13, decimal_places=7,blank=True,null=True)

