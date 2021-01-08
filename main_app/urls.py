from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('profile/', views.profile, name='profile'),
  path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
  path('message/', views.message, name='message'),
  path('message/create/', views.add_message, name='add_message'),
  path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
  path('recipients/', views.RecipientList.as_view(), name='recipient_index'),
  # path('recipients/<int:pk>/', views.RecipientDetail.as_view(), name='recipient_detail'),
  path('recipients/create/', views.RecipientCreate.as_view(), name='recipient_create'),
  path('recipients/<int:pk>/delete/', views.RecipientDelete.as_view(), name='recipient_delete'),
]