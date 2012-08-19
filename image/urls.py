from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^request/$', 'image.views.request_image', name="requestimage"),
    url(r'^offer/$', 'image.views.offer_image', name="offerimage"),
)
