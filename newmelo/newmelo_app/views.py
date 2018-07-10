from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Entry, Profile, Gspot

from django.forms import ModelForm

# Create your views here.

#MAIN SITE VIEWS

def main(request):
	return render(request, 'newmelo_app/main.html')
def home(request):
	return render(request, 'newmelo_app/home.html')
def about(request):
    return render(request, 'newmelo_app/about.html')

# USERS

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'avatar']

def userlist(request):
    users = Users.objects.all()
    return render(request, 'newmelo_app/userlist.html', {'users': users})

def createuser(request):
    form = UserForm(request.POST)
    if form.is_valid():
        form.save
        return redirect('home')
    return render(request, 'newmelo_app/createuser.html', {'form':form})

def getuser(request):
    user = User.objects.get(id=pk)
    return render(request, 'newmelo_app/user/<pk>', {'users':user})

# ENTRIES

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['id', 'title', 'body', 'user', 'tag']

def allentries(request, template_name='newmelo_app/allentries.html'):
    entries = Entry.objects.all()
    data = {}
    data['object_list'] = entries
    return render(request, template_name, {entries: entries})

def newentry(request, template_name='newmelo_app/newentry.html'):
    form = EntryForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('entries:allentries')
    return render(request, template_name, {'form':form})

def editentry(request, pk, template_name='entry/editentry.html'):
    entry = get_object_or_404(entry, pk=pk)
    form = EntryForm(request.PUT, instance=entry)
    if form.is_valid():
        form.save()
        return redirect('entries:allentries')
    return render(request, template_name, {'form': form})

def deleteentry(request, pk, template_name='entry/deleteentry.html'):
    entry = get_object_or_404(entries, pk=pk)
    if request.method=='GET':
        entry.delete()
        return redirect('entries:allentries')
    return render(request, template_name, {'object': entry})

#PROFILE

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'picture', 'quote', 'birthday', 'disposition', 'location', 'sex']

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
        return redirect('home')
    return render(request, 'newmelo_app/editprofile.html', {'form': form})

#GSPOTS

class GspotForm(ModelForm):
    class Meta:
        model = Gspot
        fields = ['gspot', 'entry']

def creategspot(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save
        return redirect('home')
    return render(request, template_name, {'form':form})

def editgspot(request, pk, template_name='gspot/gspotform.html'):
    gspot = get_object_or_404(entry, pk=pk)
    form = GspotForm(request.PUT, instance=gspot)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form': form})

def deletegspot(request, pk, template_name='entry/deletegspot.html'):
    gspot = get_object_or_404(gspots, pk=pk)
    if request.method=='GET':
        gspot.delete()
        return redirect('home')
    return render(request, template_name, {'object': gspot})
