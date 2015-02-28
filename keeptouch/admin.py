from django.contrib import admin
from keeptouch.models import User, Message, Connection

class UserAdmin(admin.ModelAdmin):
	fields = ['name', 'thumbnail', 'fb_id']

admin.site.register(User, UserAdmin)
admin.site.register(Message)
admin.site.register(Connection)
# Register your models here.
