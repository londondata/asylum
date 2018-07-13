from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm, EntryForm, GspotForm
from .models import Entry, Gspot, Profile

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


# Create your views here.

#MAIN SITE VIEWS

def hq(request):
	return render(request, 'newmelo_app/hq.html')

def frontpage(request):
	return render(request, 'newmelo_app/frontpage.html')

@login_required
def switchboard(request):
    entries = Entry.objects.all()
    return render(request, 'newmelo_app/switchboard.html', {'entries': entries})

def about(request):
    return render(request, 'newmelo_app/about.html')

# @login_required
def journal(request, pk):
	if request.user.is_authenticated:
		entries = Entry.objects.filter(user=pk)
		return render(request, 'newmelo_app/journal.html', {'entries': entries})
	else:
		form = UserCreationForm()
		return redirect(request, 'newmelo_app/signup.html', {'form':form})



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
    return render(request, 'newmelo_app/about.html', {'form': form})


def userlist(request):
    users = Users.objects.all()
    return render(request, 'newmelo_app/userlist.html', {'users': users})


def getuser(request):
    user = User.objects.get(id=pk)
    return render(request, 'newmelo_app/user/<pk>', {'users':user})


# ENTRIES
@login_required
def allentries(request):
    entries = Entry.objects.all()
    return render(request, 'newmelo_app/allentries.html', {'entries': entries})

@login_required
def newentry(request):
    author = request.user
    form = EntryForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        body = form.cleaned_data.get('body')
        user = request.user
        new_entry = Entry(title=title, body=body, user=user)
        new_entry.save()
        return redirect('switchboard')
    return render(request, 'newmelo_app/newentry.html', {'form':form})

@login_required
def editentry(request, pk):
    entry = Entry.objects.get(pk=pk)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance = entry)
        if form.is_valid:
            entry = form.save()
            return redirect('switchboard')
    else:
        form = EntryForm(instance = entry)
        return render(request, 'newmelo_app/editentry.html', {'form': form})

@login_required
def deleteentry(request, pk):
    entry = Entry.objects.get(pk=pk)
    if request.method=='POST':
        Entry.objects.get(pk = pk).delete()
        return redirect('switchboard')
    return render(request, 'newmelo_app/deleteentry.html')

# def findentry(request, pk):
#     entry = Entry.objects.get(id=pk)
#     return render(request, 'newmelo_app/entry/<int:pk>.html', {'entry': entry})

@login_required
def entrydetail(request, pk):
    entry = Entry.objects.get(id=pk)
    return render(request, 'newmelo_app/entrydetail.html', {'entry': entry})

#PROFILE
@login_required
def createprofile(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save
        return redirect('home')
    return render(request, 'newmelo_app/createprofile.html', {'form':form})

@login_required
def editprofile(request, pk, template_name='profile/profileform.html'):
    profile = get_object_or_404(profile, pk=pk)
    form = ProfileForm(request.PUT, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('switchboard')
    return render(request, 'newmelo_app/editprofile.html', {'form': form})


# GSPOTS
@login_required
def creategspot(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save
        return redirect('switchboard')
    return render(request, template_name, {'form':form})

@login_required
def editgspot(request, pk, template_name='gspot/gspotform.html'):
    gspot = get_object_or_404(entry, pk=pk)
    form = GspotForm(request.PUT, instance=gspot)
    if form.is_valid():
        form.save()
        return redirect('switchboard')
    return render(request, template_name, {'form': form})

@login_required
def deletegspot(request, pk):
    gspot = get_object_or_404(gspots, pk=pk)
    if request.method=='GET':
        gspot.delete()
        return redirect('switchboard')
    return render(request, 'entry/deletegspot.html', {'object': gspot})
