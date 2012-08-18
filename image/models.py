from django.db import models
from django.contrib.auth.models import User

class ImageRequest(models.Model):
    user = models.ForeignKey(User, related_name="image_requests")
    location = models.CharField(max_length=200)
    description = models.TextField()
    expiration = models.DateTimeField(blank=True,null=True)
    latitude = models.DecimalField(max_digits=13, decimal_places=7,blank=True,null=True)
    longitude = models.DecimalField(max_digits=13, decimal_places=7,blank=True,null=True)

