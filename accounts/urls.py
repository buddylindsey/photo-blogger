from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from django.views.generic.simple import redirect_to
from django.contrib.auth import logout as auth_logout

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    url(r'^index/$', TemplateView.as_view(template_name="accounts/index.html"), name="account_index"),
    url(r'^login/$', redirect_to, { 'url': '/accounts/login/facebook' }),
    url(r'^logout/$', auth_logout, name='logout'),
)
