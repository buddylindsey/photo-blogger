# Create your views here.
from django.shortcuts import *
from django.template import RequestContext
from image.forms import ImageRequestForm

def index(request):
    form = ImageRequestForm()
    return render_to_response('home/index.html',
            {"form":form},
            context_instance=RequestContext(request)) 

def list(request):
    form = ImageRequestForm()
    return render_to_response('home/list.html',
            {"form":form},
            context_instance=RequestContext(request)) 
