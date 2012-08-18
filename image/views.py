from django.views.generic import CreateView, UpdateView, DeleteView

from image.models import ImageRequest
from image.forms import ImageRequestForm

class RequestImageView(CreateView):
    model = ImageRequest         
    form_class = ImageRequestForm
    success_url = "/"       

class UpdateImageView(UpdateView):
    model = ImageRequest
    form_class = ImageRequestForm
    success_url = "/"

class DeleteImageView(DeleteView):
    model = ImageRequest
    success_url = "/"  


def OfferImageView(request):
    return render_to_response('image/offerimge_form.html',
            {},
            context_instance=RequestContext(request))
