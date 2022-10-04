from django.contrib import admin

from .models import Conversation,User,Message

admin.site.register(Conversation)
admin.site.register(User)
admin.site.register(Message)
