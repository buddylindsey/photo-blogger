from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class ImageRequest(models.Model):
    user = models.ForeignKey(User, related_name="image_requests")
    location = models.CharField(max_length=200)
    description = models.TextField()
    expiration = models.DateTimeField(blank=True,null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=17,blank=True,null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=17,blank=True,null=True)

        
    def non_approved_offers(self):
        offers = self.offers.filter(approval=0)
        return offers

    def approved_offers(self):
        offers = self.offers.filter(approval=1)
        return offers

    def _has_approved_image(self):
        if(self.offers.filter(approval=1).count() > 0):
            return True
        else:
            return False

    def __unicode__(self):
        return self.location

class ImageOffer(models.Model):
    user = models.ForeignKey(User, related_name="image_offers")
    request = models.ForeignKey(ImageRequest, related_name="offers")
    image = models.ImageField(upload_to="/")
    notes = models.TextField(blank=True,null=True)
    approval = models.IntegerField(default=0,blank=True)
    date_taken = models.DateTimeField(default=now(),blank=True)
