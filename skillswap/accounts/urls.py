from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('self_profile/', views.self_profile, name = 'self_profile'),
    path('profile/', views.profile, name = 'profile'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
]