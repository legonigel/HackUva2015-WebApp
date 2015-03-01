from django.conf.urls import patterns, include, url

from views import AdditionalPermissionsRedirect
from allaccess.views import OAuthCallback

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackUVA.views.home', name='home'),
    url(r'^', include('keeptouch.urls')),
	url(r'^login/(?P<provider>(\w|-)+)/$', AdditionalPermissionsRedirect.as_view(), name='allaccess-login'),
    url(r'^accounts/callback/(?P<provider>(\w|-)+)/$', OAuthCallback.as_view(), name='allaccess-callback'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
