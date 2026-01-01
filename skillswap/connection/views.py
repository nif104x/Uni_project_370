from django.shortcuts import render, redirect
from connection.queries import *
# Create your views here.
def connection_chat(request):
    username = request.session.get('username')
    requesters = db_get_connection_requests(username)
    return render(request, 'connection/chatbase.html', {'requesters':requesters,})


def send_request(request, target_user):
    sender = request.session.get('username')
    db_make_request(sender, target_user)
    return redirect('chat') 