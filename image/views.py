from django.template import RequestContext
from django.shortcuts import redirect, render_to_response
from django.views.generic import CreateView, UpdateView, DeleteView

from buddy.amazon import upload_to_s3

from image.models import ImageRequest
from image.forms import ImageRequestForm, ImageOfferForm

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


def offer_image(request):
    if request.method == "POST":
        form = ImageOfferForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['image']

            filename = upload_to_s3(file, 'dash-media')

            form.image = filename
            io = form.save()

            return redirect(reverse('index'))
        else:
            return render_to_response('image/imageoffer_form.html',
                {'form':form},
                context_instance=RequestContext(request))

    else:
        form = ImageOfferForm()
        return render_to_response('image/imageoffer_form.html',
            {'form':form},
            context_instance=RequestContext(request))

