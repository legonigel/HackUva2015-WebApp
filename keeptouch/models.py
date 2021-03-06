from django.db import models

# Create your models here.

class User(models.Model):
	name 		= models.CharField(max_length=40)
	thumbnail 	= models.URLField(blank=True)
	fb_id		= models.CharField(max_length=100)
	is_online	= models.BooleanField(default=False)
	friends		= models.ManyToManyField('self', blank=True)

	def __str__(self):
		onlineStr = ':online' if self.is_online else ':offline'
		return self.name + " ID:" + self.fb_id + onlineStr

class Conversation(models.Model):
	user1			= models.ForeignKey(User, related_name="user1")
	user2			= models.ForeignKey(User, related_name="user2")
	user1_name		= models.CharField(max_length=40)
	user2_name		= models.CharField(max_length=40)
	timestamp		= models.DateTimeField('last published')
	is_read			= models.BooleanField(default=False)
	last_message	= models.CharField(max_length=256, blank=True)

	def __str__(self):
		return "Users: " + str(self.user1.pk) + "," + str(self.user2.pk) + " last_message:" + self.last_message + (':read' if self.is_read else ':unread')

class Message(models.Model):
	is_read			= models.BooleanField(default=False)
	timestamp		= models.DateTimeField('date published')
	message_text	= models.CharField(max_length=256)
	sender			= models.ForeignKey(User, related_name="sender")
	reciever		= models.ForeignKey(User, related_name="reciever")
	conversation 	= models.ForeignKey(Conversation, related_name="conversation", default='1')

	def __str__(self):
		return self.message_text + ", to " + self.reciever.name + " from " + self.sender.name
	

class Connection(models.Model):
	user		= models.ForeignKey(User)
	token		= models.CharField(max_length=500)
	expiration 	= models.IntegerField()
	status 		= models.CharField(max_length=100)

	def __str__(self):
		return self.user.name + " is connected with token: " + self.token
	
