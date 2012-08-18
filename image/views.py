from django.views.generic import CreateView, UpdateView, DeleteView

from image.models import Image
from image.forms import ImageForm

class AddImageView(CreateView):
    model = Image         
    form_class = ImageForm
    success_url = "/"       

class UpdateImageView(UpdateView):
    model = Image               
    form_class = ImageForm
    success_url = "/"

class DeleteImageView(DeleteView):
    model = Image 
    success_url = "/"  
