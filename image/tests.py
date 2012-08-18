from django.test import TestCase
from django.conf import settings
from django.utils.timezone import now
from django.core.urlresolvers import reverse

from image.models import Image
from image.forms import ImageForm

class ImageModelTest(TestCase):
    def test_model_field(self):
        img = Image()
        img.location = "Downtown Tulsa"
        img.description = "Williams Tower"
        img.expiration = now()
        img.latitude = 35.987628
        img.longitude = -96.114063
        
        img.save()

        self.assertEqual(img.id, Image.objects.get(location__exact="Downtown Tulsa").id)


class ImageFormTest(TestCase):
    def test_required_description_field(self):
        imageform = ImageForm(data={"description":"Tulsa"})
        imageform.is_valid()

        self.assertEqual(imageform.errors['location'], [u'This field is required.'])

    def test_required_location_field(self):
        imageform = ImageForm(data={"location":"Tulsa"})
        imageform.is_valid()

        self.assertEqual(imageform.errors['description'], [u'This field is required.'])


    def test_add_data_through_form(self):
        response = self.client.post(reverse("requestimage"), {"location":"tulsa","description":"other"})

        # Uncomment once index page exists
        #self.assertRedirects(response, "/")
        self.assertEqual(1, Image.objects.get(location__exact="tulsa").id)

