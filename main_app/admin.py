from django.contrib import admin
from .models import Profile, Message, Business, Recipient

# Register your models here.
admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Business)
admin.site.register(Recipient)
