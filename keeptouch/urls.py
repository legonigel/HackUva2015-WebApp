from django.conf.urls import patterns, url

from keeptouch import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)
