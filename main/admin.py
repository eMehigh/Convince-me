from django.contrib import admin

# Register your models here.
from .models import Room, CreatorMessages, JoinerMessages
admin.site.register(Room)
admin.site.register(CreatorMessages)
admin.site.register(JoinerMessages)