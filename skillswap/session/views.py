from django.shortcuts import render, redirect
from datetime import datetime
import uuid
from session.queries import *
from connection.queries import *
from skillEngine.queries import *

from django.utils import timezone
# Create your views here.
def view_session(request):
    username = request.session.get('username')
    connection = db_get_connection_list(username)
    all_skill = db_get_all_user_skills(username)
    teach = [s[0] for s in all_skill if s[1] == 'TEACH']
    learn = [s[0] for s in all_skill if s[1] == 'LEARN']
    sessions_data = db_get_active_sessions(username)
    pending_sessions = db_get_pending_sessions(username)


    if request.method == "POST":
        user = request.POST.get('user')
        offer = request.POST.get('offer')
        rqst = request.POST.get('rqst')
        date = request.POST.get('date')
        time = request.POST.get('time')
        schedule_time = datetime.strptime(
            f"{date} {time}", "%Y-%m-%d %H:%M"
        )
        session_id = str(uuid.uuid4())[:8]
        db_create_session(username, user, offer, rqst, schedule_time, session_id)
        return redirect('view_session')

    return render(request, 'session/session.html', 
                  {'username': username,
                   'connection': connection,
                   'teach': teach,
                   'learn': learn,
                   'sessions': sessions_data,
                   'pending_sessions': pending_sessions,
                   'now_time': timezone.localtime(),
                  })


# def make_session_request(request):
#     username = request.session.get('username')

#     if request.method == "POST":
#         user = request.POST.get('user')
#         offer = request.POST.get('offer')
#         rqst = request.POST.get('rqst')
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         schedule_time = datetime.strptime(
#             f"{date} {time}", "%Y-%m-%d %H:%M"
#         )
#         session_id = str(uuid.uuid4())[:8]
#         db_create_session(username, user, offer, rqst, schedule_time, session_id)



def accept_session_request(request, s_id):
    username = request.session.get('username')
    link = f"https://meet.jit.si/{s_id}"
    db_accept_session(link, s_id)
    return redirect('view_session')

def decline_session_request(request, s_id):
    db_delete_session(s_id)
    return redirect('view_session')

def cancel_session_request(request, s_id):
    db_delete_session(s_id)
    return redirect('view_session')

def join(request, link):
    return render(request, 'session/meeting.html', {'link':link})


def complete_session(request, s_id):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE session SET status = 'completed' WHERE session_id = %s", [s_id])
    
    username = request.session.get('username')
    db_process_session_credits(username)
    
    return redirect('view_session')