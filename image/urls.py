from django.conf.urls.defaults import *

from image.views import RequestImageView

urlpatterns = patterns('',
    url(r'^request/$', RequestImageView.as_view(), name="requestimage"),
    url(r'^offer/$', 'image.views.offer_image', name="offerimage"),
)
