from django.urls import path
from . import views

urlpatterns = [
    path('chatbox/', views.connection_chat, name = 'chat'),
]