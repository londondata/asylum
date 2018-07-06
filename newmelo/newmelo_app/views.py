from django.shortcuts import render
from .models import User, Post, Profile, Gspot

# Create your views here.

# USERS
def userlist(request):
    users = Users.objects.all()
    return render(request, 'newmelo/userlist.html', {'users': users})
