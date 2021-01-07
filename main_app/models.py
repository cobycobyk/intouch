from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=150)
    domain = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    invite = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('business', kwargs={'business_id': self.id})

class Profile(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    ph_number = PhoneField(null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_id': self.id})


class Message(models.Model):
    date = models.DateTimeField('Send Date')
    content = models.TextField(max_length=280)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)

    def get_absolute_url(self):
        return reverse('message', kwargs={'message_id': self.id})

class Recipient(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    ph_number = PhoneField(null=False, blank=False)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, default=None, blank=True, null=True)
