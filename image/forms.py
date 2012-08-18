from django.forms import ModelForm

from image.models import Image

class ImageForm(ModelForm):
    class Meta:
        model = Image
