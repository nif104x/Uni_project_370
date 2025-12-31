from django.shortcuts import render
from . import queries
# Create your views here.
def profile_grid(request, username=None):
    if username!=None:
        profile = queries.get_profile(username)
        return render(request,'accounts/profile.html', {'profile':profile, 'username':username})
    return render(request, 'skillEngine/profile_grid.html')



def view_profile(request, username):
    profile = queries.get_profile(username)
    return render(request,'accounts/profile.html', {'profile':profile, 'username':username})
