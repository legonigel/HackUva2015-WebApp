from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackUVA.views.home', name='home'),
    url(r'^', include('keeptouch.urls')),
	
	url(r'^accounts/', include('allaccess.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
