from django.conf.urls.defaults import *
from django.views.generic import TemplateView, ListView
from django.views.generic.simple import redirect_to
from django.contrib.auth import logout as auth_logout

from image.models import ImageRequest

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    url(r'^index/$', TemplateView.as_view(template_name="accounts/index.html"), name="account_index"),
    url(r'^login/$', redirect_to, { 'url': '/accounts/login/facebook' }, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="logout"),
    url(r'^review/$', ListView.as_view(
            template_name="accounts/review.html",
            context_object_name="requests",
            model=ImageRequest
        ), name="reviewrequests"),
    #url(r'^$', redirect_to, { 'url': '/' }),
)
