# Create your views here.
from django.shortcuts import render, redirect
from .queries import db_admin_get_stats, db_admin_delete

def admin_dashboard(request):
    # Optional: Check if user is actually an admin
    if request.session.get('username') != 'admin':
        # return redirect('dashboard') 
        pass

    if request.method == "POST":
        target_table = request.POST.get('table')
        pk_column = request.POST.get('pk_col')
        pk_value = request.POST.get('pk_val')
        
        db_admin_delete(target_table, pk_column, pk_value)
        return redirect('admin_panel')

    users, sessions = db_admin_get_stats()
    return render(request, 'Owner/adminPanel.html', {
        'users': users,
        'sessions': sessions
    })