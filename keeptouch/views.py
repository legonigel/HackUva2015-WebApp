from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from keeptouch.models import User, Conversation

# Create your views here.

def index(request):
	context = {}
	if request.user.is_authenticated():	
		try:
			access = request.user.accountaccess_set.all()[0]
		except IndexError:
			access = None
		else:
			client = access.api_client
			profile_info = client.get_profile_info(raw_token=access.access_token)
			context['info'] = profile_info
			user = User.objects.filter(fb_id=profile_info.get('id'))[0]
		convo_list = Conversation.objects.filter(user1=user) | Conversation.objects.filter(user2=user)
		context['conversation_list'] = convo_list
		thumb_list = []
		for convo in convo_list:
			if convo.user1 == user:
				other_user = convo.user2
			else:
				other_user = convo.user1
			thumb_list.append(str("http://graph.facebook.com/" + str(other_user.fb_id) + "/picture?type=square"))
		context['convo_w_thumb'] = zip(convo_list, thumb_list)
	return render(request, "index.html", context)

def thread(request):
	context={}

	return render(request, "thread.html", context)

def handle_login(request):
	if request.user.is_authenticated():	
		try:
			access = request.user.accountaccess_set.all()[0]
		except IndexError:
			access = None
		else:
			client = access.api_client
			profile_info = client.get_profile_info(raw_token=access.access_token)
			user = User.objects.filter(fb_id=profile_info.get('id'))
			if user is None: 
				thumb = "http://graph.facebook.com/" + profile_info.get('id') + "/picture?type=square"
				friends = []
				friendslist = client.request('get', "https://graph.facebook.com/v2.2/me/friends").json().get('data')
				for person in friendslist:
					friends.append(User.objects.filter(fb_id=person.get('id')))
				user = User(name=profile_info.get('name'), 
					thumbnail=thumb, fb_id=profile_info.get('id'), is_online=false, friends=friends)
	return render(request, "index.html", context)


