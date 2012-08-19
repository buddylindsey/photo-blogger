from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^request/(?P<id>\d+)/offers/$', 'image.ajax.request_offers', name="requestoffers"),
    url(r'^request/(?P<id>\d+)/$', 'image.ajax.request_details', name="requestdetails"),
    url(r'^request/$', 'image.views.request_image', name="requestimage"),
    url(r'^offer/$', 'image.views.offer_image', name="offerimage"),
)
