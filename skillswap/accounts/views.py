from django.shortcuts import render, redirect
from accounts.forms import*
from accounts.queries import*
# Create your views here.



#REGISTRATION

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





#LOGIN
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





#DASHBOARD

def dashboard(request):
    username = request.session.get('username')
    if not username:
        return redirect('/account/login/')
    
    profile = get_user_full_profile(username)

    return render(request, 'accounts/dashboard.html', {'profile':profile})




#SELF_PROFILE
def self_profile(request):
    username = request.session.get('username')

    if request.method == 'POST':

        if "edit-bio" in request.POST:
            form = user_bio(request.POST)
            if form.is_valid():
                new_bio = form.cleaned_data["bio"]
                db_update_bio(username, new_bio)
            return redirect('/account/self_profile/')

        elif "teach" in request.POST:
            form = user_skill(request.POST)
            if form.is_valid():
                skill_id = form.cleaned_data["skill_id"]
                db_update_skill(username, skill_id, "TEACH")
            return redirect('/account/self_profile/')

        elif "learn" in request.POST:
            form = user_skill(request.POST)
            if form.is_valid():
                skill_id = form.cleaned_data["skill_id"]
                db_update_skill(username, skill_id, "LEARN")
            return redirect('/account/self_profile/')

        elif "u_email" in request.POST:
            form = user_email(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                db_update_email(username, email)
            return redirect('/account/self_profile/')
        
        elif "u_password" in request.POST:
            form = user_password(request.POST)
            if form.is_valid():
                password = form.cleaned_data["password"]
                db_update_password(username, password)
            return redirect('/account/self_profile/')

    profile = get_user_full_profile(username)
    skill = db_get_all_skills()      

    return render(request, 'accounts/self_profile.html', {'profile': profile, 'username': username, 'skill':skill})





#PUBLIC VIEW PROFILE

def profile(request):
    return render(request, 'accounts/profile.html')