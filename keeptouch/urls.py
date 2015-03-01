from django.conf.urls import patterns, url

from keeptouch import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^thread/(?P<conversation_id>\d+)/$', views.thread),
	url(r'^thread/(?P<conversation_id>\d+)/reply/$', views.reply, name='reply'),
	url(r'^mkthread/(?P<other_user_id>\d+)/$', views.mkthread),
	url(r'^contacts/', views.contacts),
	url(r'^handle_login/', views.handle_login, name='handle_login'),
)
