from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from keeptouch.models import User, Conversation, Message
import datetime

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
			context['myuser']=user
		convo_list = Conversation.objects.filter(user1=user) | Conversation.objects.filter(user2=user)
		context['conversation_list'] = convo_list
		thumb_list = []
		other_user_list = []
		for convo in convo_list:
			if convo.user1 == user:
				other_user = convo.user2
			else:
				other_user = convo.user1
			other_user_list.append(other_user)
			thumb_list.append(str("http://graph.facebook.com/" + str(other_user.fb_id) + "/picture?type=square"))
		context['convo_w_thumb'] = zip(convo_list, thumb_list, other_user_list)
	return render(request, "index.html", context)

def thread(request, conversation_id=0):
	context={}

	if request.user.is_authenticated():	
		try:
			access = request.user.accountaccess_set.all()[0]
		except IndexError:
			access = None
		else:
			client = access.api_client
			profile_info = client.get_profile_info(raw_token=access.access_token)
			context['info'] = profile_info
			user = User.objects.get(fb_id=profile_info.get('id'))
			print int(conversation_id)
		try:
			convo = Conversation.objects.get(id=int(conversation_id))
		except Conversation.DoesNotExist:
			raise Http404("Conversation does not exist")

		if(user == convo.user1):
			other_user = convo.user2
		else:
			other_user = convo.user1
		context['me'] = user
		context['other_user'] = other_user
		msg_list = Message.objects.filter(sender=user, reciever=other_user) | Message.objects.filter(reciever=user, sender=other_user)

		context['conversation_list'] = msg_list
		thumb_list = []
		is_sender_list = []
		for msg in msg_list:
			thumb_list.append(str("http://graph.facebook.com/" + str(msg.sender.fb_id) + "/picture?type=square"))
			msg.is_read = True;
			is_sender_list.append(msg.sender==user)
		context['msg_w_thumb'] = zip(msg_list, thumb_list, is_sender_list)

	return render(request, "thread.html", context)

def reply(request, conversation_id):
	convo = get_object_or_404(Conversation, pk=conversation_id)
	try:
		access = request.user.accountaccess_set.all()[0]
	except IndexError:
		access = None
	else:
		client = access.api_client
		profile_info = client.get_profile_info(raw_token=access.access_token)
		user = User.objects.filter(fb_id=profile_info.get('id'))[0]	
	if(user == convo.user1):
		other_user = convo.user2
	else:
		other_user = convo.user1
	message = request.POST['message']
	m = Message(timestamp=datetime.datetime.now(), message_text= message, 
		sender = user, reciever=other_user, conversation=convo )
	m.save()
	convo.last_message = message
	convo.save()
	return HttpResponseRedirect('..')

def contacts(request):
	context={}
	try:
		access = request.user.accountaccess_set.all()[0]
	except IndexError:
		access = None
	else:
		client = access.api_client
		profile_info = client.get_profile_info(raw_token=access.access_token)
		user = User.objects.filter(fb_id=profile_info.get('id'))[0]	
	friends = user.friends.all()
	thumb_list = []
	for friend in friends:
		thumb_list.append(str("http://graph.facebook.com/" + str(friend.fb_id) + "/picture?type=square"))
	context['friend_w_thumb']= zip(friends, thumb_list)
	
	return render(request, "contact.html", context)

def mkthread(request, other_user_id):
	context={}
	try:
		access = request.user.accountaccess_set.all()[0]
	except IndexError:
		access = None
	else:
		client = access.api_client
		profile_info = client.get_profile_info(raw_token=access.access_token)
		user = User.objects.filter(fb_id=profile_info.get('id'))[0]	
	other_user=User.objects.get(fb_id=other_user_id)
	convo_set = Conversation.objects.filter(user1=user, user2=other_user) | Conversation.objects.filter(user2=user, user1=other_user)
	if not convo_set:
		convo = Conversation(user1=user, user2=other_user, user1_name=user.name, user2_name=other_user.name, timestamp=datetime.datetime.now(),
			last_message='')
		convo.save()
	else:
		convo = convo_set[0]
	return HttpResponseRedirect('/thread/' + str(convo.id) + '/')

def handle_login(request):
	context={}
	if request.user.is_authenticated():	
		try:
			access = request.user.accountaccess_set.all()[0]
		except IndexError:
			access = None
		else:
			client = access.api_client
			profile_info = client.get_profile_info(raw_token=access.access_token)
			user = User.objects.filter(fb_id=profile_info.get('id'))
			if not user:
				u = User(name=profile_info.get('name'), thumbnail='', fb_id=profile_info.get('id'))				
				u.save()
				friends =[]
				friendslist = client.request('get', "https://graph.facebook.com/v2.2/me/friends").json().get('data')
				print friendslist
				for person in friendslist:
					u.friends.add(User.objects.get(fb_id=person.get('id'))) 


	return HttpResponseRedirect('/')

