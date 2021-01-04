from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm
from .models import Profile


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def profile(request):
  profile = Profile.objects.get(user=request.user)
  return render(request, 'profile.html', {'profile': profile})


# class ProfileCreate(LoginRequiredMixin, CreateView):
#   model = Profile
#   fields = '__all__'

#   def form_valid(self, form):
#     form.instance.user = self.request.user
#     form.instance.city = self.request.city
#     form.instance.state = self.request.state
#     form.instance.ph_number = self.request.ph_number
#     return super().form_valid(form)

#   success_url = '/profile/'

# class ProfileEdit(UpdateView):
#   model = Profile
#   fields = '__all__'


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
      return redirect('edit_profile', user_id=user_id)
    else:
      error_message = 'Invalid sign up - try again'
  # a bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)    



# def edit_profile(request, user_id):
#   profile = Profile.objects.get(id=user_id)
#   error_message = ''
#   if request.method == 'POST':
#     #this is how to create a 'user' form object
#     # that includes the data from the browser
#     form = ProfileForm(request.POST)
#     if form.is_valid():
#       profile_edit = form.save(commit=False)
#       profile_edit.user_id = user_id
#       profile_edit.save()
#     return redirect('profile', user_id=user_id)  