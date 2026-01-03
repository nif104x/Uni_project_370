from django.shortcuts import render, redirect
from connection.queries import *
from connection.forms import *
# Create your views here.
def connection_chat(request):
    username = request.session.get('username')
    requesters = db_get_connection_list(username)
    return render(request, 'connection/chatbase.html', {'requesters':requesters,})


def send_request(request, target_user):
    sender = request.session.get('username')
    db_make_request(sender, target_user)
    return redirect('chat') 

def load_conversation(request, user2):
    user1 = request.session.get('username')

    if request.method == 'POST':
        # form = textT(request.POST)
        # text = form.cleaned_data['username']
        text = request.POST.get('message')
        if text:
            send_message(user1, user2, text)
            # Redirecting to the same page to prevent duplicate messages on refresh
            return redirect('load_conversation', user2=user2)

    requesters = db_get_connection_list(user1)
    convo = get_all_messages(user1, user2)
    return render(request, 'connection/chatbase.html', {'requesters':requesters, 'convo': convo, 'user1':user1, 'user2': user2})



