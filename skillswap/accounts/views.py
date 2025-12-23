from django.shortcuts import render, redirect
from accounts.forms import*
from accounts.queries import*
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = registration(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            db_registration(username, password, name, email)
            return redirect('/account/login/')

    else:
        form = registration()

    return render(request, 'accounts/register.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = login_form(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            role = get_user_role(username, password)

            if role =='admin':
                request.session['username'] = username
                return None
            
            elif role=='user':
                request.session['username'] = username
                return redirect('/account/dashboard/')
            
            else:
                return render(request, 'accounts/login.html', {'error': 'Wrong username or password'})

    return render(request, 'accounts/login.html')

def dashboard(request):
    username = request.session.get('username')
    
    if not username:
        return redirect('/account/login/')



    return render(request, 'accounts/dashboard.html')

def self_profile(request):
    return render(request, 'accounts/self_profile.html')

def profile(request):
    return render(request, 'accounts/profile.html')