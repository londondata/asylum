from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, ProfileForm, EntryForm, GspotForm
from .models import User, Entry, Gspot, Profile

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

#MAIN SITE VIEWS

def hq(request):
	return render(request, 'newmelo_app/hq.html')
def switchboard(request):
	return render(request, 'newmelo_app/switchboard.html')
def about(request):
    return render(request, 'newmelo_app/about.html')
def journal(request):
    return render(request, 'newmelo_app/journal.html')

# USERS

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('hq')
    else:
        form = UserCreationForm()
    return render(request, 'newmelo_app/signup.html', {'form': form})

def userlist(request):
    users = Users.objects.all()
    return render(request, 'newmelo_app/userlist.html', {'users': users})

# def createuser(request):
#     form = UserForm(request.POST)
#     if form.is_valid():
#         form.save
#         return redirect('home')
#     return render(request, 'newmelo_app/createuser.html', {'form':form})

def getuser(request):
    user = User.objects.get(id=pk)
    return render(request, 'newmelo_app/user/<pk>', {'users':user})

# ENTRIES

def allentries(request):
    entries = Entry.objects.all()
    data = {}
    data['object_list'] = entries
    return render(request, 'newmelo_app/allentries.html', {'entries': entries})

def newentry(request, template_name='newmelo_app/newentry.html'):
    form = EntryForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('switchboard')
    return render(request, template_name, {'form':form})

def editentry(request, pk):
    entry = Entry.objects.get(pk=pk)
    form = EntryForm(request.POST, instance=entry)
    if form.is_valid():
        form.save()
        return redirect('switchboard')
    return render(request, 'newmelo_app/editentry.html', {'form': form})

def deleteentry(request, pk, template_name='newmelo_app/deleteentry.html'):
    entry = get_object_or_404(entries, pk=pk)
    if request.method=='GET':
        entry.delete()
        return redirect('switchboard')
    return render(request, template_name, {'object': entry})

def findentry(request, pk, template_name='newmelo_app/entry/<int:pk>.html'):
    entry = Entry.objects.get(id=pk)
    return render(request, template_name, {'entry': entry})

def entrydetail(request, pk):
    entry = Entry.objects.get(id=pk)
    return render(request, 'newmelo_app/entrydetail.html', {'entry': entry})

#PROFILE

def createprofile(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save
        return redirect('home')
    return render(request, 'newmelo_app/createprofile.html', {'form':form})

def editprofile(request, pk, template_name='profile/profileform.html'):
    profile = get_object_or_404(profile, pk=pk)
    form = ProfileForm(request.PUT, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('switchboard')
    return render(request, 'newmelo_app/editprofile.html', {'form': form})


# GSPOTS

def creategspot(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save
        return redirect('switchboard')
    return render(request, template_name, {'form':form})

def editgspot(request, pk, template_name='gspot/gspotform.html'):
    gspot = get_object_or_404(entry, pk=pk)
    form = GspotForm(request.PUT, instance=gspot)
    if form.is_valid():
        form.save()
        return redirect('switchboard')
    return render(request, template_name, {'form': form})

def deletegspot(request, pk, template_name='entry/deletegspot.html'):
    gspot = get_object_or_404(gspots, pk=pk)
    if request.method=='GET':
        gspot.delete()
        return redirect('switchboard')
    return render(request, template_name, {'object': gspot})
