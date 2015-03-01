from django.conf.urls import patterns, url

from keeptouch import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^handle_login', views.handle_login, name='handle_login')
)
