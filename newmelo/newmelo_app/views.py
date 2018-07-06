from django.shortcuts import render
from .models import User, Post, Profile, Gspot

from django.forms import ModelForm

# Create your views here.

# USERS
def userlist(request):
    users = Users.objects.all()
    return render(request, 'newmelo/userlist.html', {'users': users})


# ENTRIES

class EntryForm(ModelForm):
    class Meta:
        model = post
        fields = ['id', 'title', 'body', 'user', 'tag', 'created']

def entrylist(request):
    entries = entry.objects.all()
    data = {}
