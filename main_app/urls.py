from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('profile/', views.profile, name='profile'),
  path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
  # path('profile/<int:pk>/edit/', views.ProfileEdit.as_view(), name='edit_profile'),
]