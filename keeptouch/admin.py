from django.contrib import admin
from keeptouch.models import User, Message, Connection, Conversation

class UserAdmin(admin.ModelAdmin):
	fields = ['name', 'thumbnail', 'fb_id', 'friends']

admin.site.register(User, UserAdmin)
admin.site.register(Message)
admin.site.register(Connection)
admin.site.register(Conversation)
# Register your models here.
