from django.urls import path
from . import views

urlpatterns = [
    # Add your user endpoints here
    path('profile/update/', views.profile_update, name='profile_update'),
] 