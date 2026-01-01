from django.urls import path
from . import views

urlpatterns = [
    path('connect/', views.connection_chat, name='chat'),
    path('connect/<str:target_user>/', views.send_request, name='send_request'),
]