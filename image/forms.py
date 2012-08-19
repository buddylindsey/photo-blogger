from django import forms

from image.models import ImageRequest, ImageOffer

class ImageRequestForm(forms.ModelForm):
    location = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder':'Tulsa, Ok'}))
    expiration = forms.DateField(required=False, widget=forms.DateInput(format='%m/%d/%Y',attrs={'placeholder':'12/25/2012'}))
    latitude = forms.DecimalField(required=False, max_digits=13, decimal_places=7,widget=forms.HiddenInput())
    longitude = forms.DecimalField(required=False, max_digits=13, decimal_places=7,widget=forms.HiddenInput())

    class Meta:
        exclude = ('user',)
        model = ImageRequest

class ImageOfferForm(forms.ModelForm):

    class Meta:
        exclude = ('request', 'user', 'approval', 'date_taken')
        model = ImageOffer
