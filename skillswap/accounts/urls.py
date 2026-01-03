# app_name = 'accounts'
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('self_profile/', views.self_profile, name = 'self_profile'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('profile/<str:username>/', views.get_profile, name='profile_detail'),
    path('remove_skill/<path:skill>/', views.remove_skill, name='remove_skill')
]