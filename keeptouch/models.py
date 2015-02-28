from django.db import models

# Create your models here.

class User(models.Model):
	name 		= models.CharField(max_length=40)
	thumbnail 	= models.URLField()
	fb_id		= models.CharField(max_length=100)
	is_online	= models.BooleanField(default=False)

	def __str__(self):
		onlineStr = ':online' if self.is_online else ':offline'
		return self.name + " ID:" + self.fb_id + onlineStr

class Message(models.Model):
	is_read			= models.BooleanField(default=False)
	timestamp		= models.DateTimeField('date published')
	message_text	= models.CharField(max_length=256)
	sender			= models.ForeignKey(User, related_name="sender")
	reciever		= models.ForeignKey(User, related_name="reciever")

	def __str__(self):
		return self.message_text + ", to " + self.reciever.name + " from " + self.sender.name

class Connection(models.Model):
	user		= models.ForeignKey(User)
	token		= models.CharField(max_length=500)
	expiration 	= models.IntegerField()
	status 		= models.CharField(max_length=100)

	def __str__(self):
		return self.user.name + " is connected with token: " + self.token
	
	
