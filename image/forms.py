from django.forms import ModelForm

from image.models import ImageRequest, ImageOffer

class ImageRequestForm(ModelForm):
    class Meta:
        model = ImageRequest

class ImageOfferForm(ModelForm):
    class Meta:
        model = ImageOffer
