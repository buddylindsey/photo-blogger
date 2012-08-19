from django.http import Http404
from django.core import serializers
from django.http import HttpResponse

from image.models import ImageRequest, ImageOffer


def request_details(request, id):
    if(request.method == 'GET'):
        ir = ImageRequest.objects.filter(pk=id)

        json_serializer = serializers.get_serializer("json")()
        return HttpResponse(json_serializer.serialize(ir), content_type='application/json')
    else:
        raise Http404

def request_offers(request, id):
    if(request.method == 'GET'):
        io = ImageOffer.objects.filter(request=ImageRequest.objects.get(pk=id))

        json_serializer = serializers.get_serializer("json")()
        return HttpResponse(json_serializer.serialize(io), content_type='application/json')
    else:
        raise Http404

