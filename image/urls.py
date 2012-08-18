from django.conf.urls.defaults import *

from image.views import AddImageView

urlpatterns = patterns('',
    url(r'^request/$', AddImageView.as_view(), name="requestimage"),
)
