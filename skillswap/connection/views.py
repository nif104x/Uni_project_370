from django.shortcuts import render

# Create your views here.
def connection_chat(request):
    return render(request, 'connection/chatroom.html')