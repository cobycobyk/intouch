from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    ph_number = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_id': self.id})
   

    