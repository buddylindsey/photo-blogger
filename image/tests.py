from django.test import TestCase
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from image.models import ImageRequest
from image.forms import ImageRequestForm

class ImageModelTest(TestCase):
    def _create_user(self, username, password):
        return User.objects.create_user(username=username, password=password)

    def test_model_field(self):
        user = self._create_user('buddy', 'password')

        img = ImageRequest()
        img.user = user
        img.location = "Downtown Tulsa"
        img.description = "Williams Tower"
        img.expiration = now()
        img.latitude = 35.987628
        img.longitude = -96.114063
        
        img.save()

        self.assertEqual(img.id, ImageRequest.objects.get(location__exact="Downtown Tulsa").id)


class ImageRequestFormTest(TestCase):
    def _create_user(self, username, password):
        return User.objects.create_user(username=username, password=password)

    def test_required_description_field(self):
        imageform = ImageRequestForm(data={"description":"Tulsa"})
        imageform.is_valid()

        self.assertEqual(imageform.errors['location'], [u'This field is required.'])

    def test_required_location_field(self):
        imageform = ImageRequestForm(data={"location":"Tulsa"})
        imageform.is_valid()

        self.assertEqual(imageform.errors['description'], [u'This field is required.'])


    def test_add_data_through_form(self):
        user = self._create_user('buddy', 'password')
        response = self.client.post(reverse("requestimage"), {
            "location":"tulsa",
            "description":"other",
            "user":user.id
        })

        # Uncomment once index page exists
        self.assertRedirects(response, "/")

