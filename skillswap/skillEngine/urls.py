from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.profile_grid, name = 'profile_grid'),
    path('profile/<str:username>/', views.view_profile, name='view_profile')
]