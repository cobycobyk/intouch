from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView , DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MessageForm
from .models import Profile, Message , Recipient
from datetime import date
from twilio.rest import Client
import os


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def profile(request):
  profile = Profile.objects.get(user=request.user)
  return render(request, 'profile.html', {'profile': profile})

class ProfileCreate(LoginRequiredMixin, CreateView):
  model = Profile
  fields = ['city', 'state', 'ph_number']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

  success_url = '/profile/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    #this is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      #this is how we log a user in via code
      login(request, user)
      return redirect('profile_create')
    else:
      error_message = 'Invalid sign up - try again'
  # a bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)    

@login_required
def message(request):
  profile = Profile.objects.get(user=request.user)
  message_form = MessageForm()
  recipients = Recipient.objects.all
  return render(request, 'message.html', {
    'profile': profile, 'message_form': message_form,
    'recipients': recipients
  })

@login_required
def add_message(request):
  profile = Profile.objects.get(user=request.user)
  recipients = request.POST.getlist('recipients')
  for recipient in recipients:
    account_sid = os.environ['ACCOUNT_SID']
    auth_token = os.environ['AUTH_TOKEN']
    print(account_sid, auth_token)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    to=recipient,
    from_='+14693789344',
    body=request.POST['content']
    )
    print(message.sid)
  new_message = Message(
    date = date.today(),
    content = request.POST['content'],
    profile = profile,
  )
  new_message.save()
  return redirect('message')




class ProfileUpdate(LoginRequiredMixin, UpdateView):
  model = Profile
  fields = ['city', 'state', 'ph_number']

  success_url = '/profile/'

# class BusinessCreate(LoginRequiredMixin, CreateView):
#   model = Business
#   fields = '__all__'

class RecipientCreate(LoginRequiredMixin, CreateView):
  model = Recipient
  fields = ['name', 'email', 'ph_number']
  
  def form_valid(self, form):
    return super().form_valid(form)

  success_url = '/recipients/create/'

class RecipientList(LoginRequiredMixin, ListView):
  model = Recipient

class RecipientDelete(LoginRequiredMixin, DeleteView):
  model = Recipient

  success_url = '/recipients/'
class RecipientDetail(LoginRequiredMixin,DetailView):
  model = Recipient