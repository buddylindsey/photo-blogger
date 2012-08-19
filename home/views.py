# Create your views here.
from django.shortcuts import *
from django.template import RequestContext
from image.forms import ImageRequestForm
from image.forms import ImageOfferForm
from image.models import ImageRequest

def index(request):
    form = ImageRequestForm()
    return render_to_response('home/index.html',
            {"form":form},
            context_instance=RequestContext(request)) 

def list(request):
    requestform = ImageRequestForm()
    offerform = ImageOfferForm()
    requests = ImageRequest.objects.all()
    return render_to_response('home/list.html',
            {"requestform":requestform, "offerform":offerform, "requests":requests},
            context_instance=RequestContext(request)) 
