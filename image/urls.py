from django.conf.urls.defaults import *

from image.views import AddImageView

urlpatterns = patterns('',
    url(r'^request/$', RequestImageView.as_view(), name="requestimage"),
)
