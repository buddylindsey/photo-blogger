from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class ImageRequest(models.Model):
    user = models.ForeignKey(User, related_name="image_requests")
    location = models.CharField(max_length=200)
    description = models.TextField()
    expiration = models.DateTimeField(blank=True,null=True)
    latitude = models.DecimalField(max_digits=13, decimal_places=7,blank=True,null=True)
    longitude = models.DecimalField(max_digits=13, decimal_places=7,blank=True,null=True)

class ImageOffer(models.Model):
    user = models.ForeignKey(User, related_name="image_offers")
    request = models.ForeignKey(ImageRequest, related_name="offers")
    image = models.ImageField(upload_to="/")
    notes = models.TextField(blank=True,null=True)
    approval = models.IntegerField(default=0,blank=True)
    date_taken = models.DateTimeField(default=now(),blank=True)
