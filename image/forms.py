from django.forms import ModelForm

from image.models import ImageRequest

class ImageRequestForm(ModelForm):
    class Meta:
        model = ImageRequest
