from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Post, Profile, Gspot

from django.forms import ModelForm

# Create your views here.

# USERS
def userlist(request):
    users = Users.objects.all()
    return render(request, 'newmelo_app/userlist.html', {'users': users})

# ENTRIES

class EntryForm(ModelForm):
    class Meta:
        model = post
        fields = ['id', 'title', 'body', 'user', 'tag', 'created']

def allentries(request, template_name='entry/allentries.html'):
    entries = entry.objects.all()
    data = {}
    data['object_list'] = entries
    return render(request, template_name, data)

def newentry(request):
    form = EntryForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(entry:entrylist)
    return render(request, template_name, {'form':form})

def editentry(request, pk, template_name='entry/entryform.html'):
    entry = get_object_or_404(entry, pk=pk)
    form = EntryForm(request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect(entry:entrylist)
    return render(request, template-name, {'form': form})

def deleteentry(request, pk, template_name='entry/deleteentry.html'):
    entry = get_object_or_404(entries, pk=pk)
    if request.methof=='POST':
        entry.delete()
        return redirect('entries:allentries')
    return render(request, template_name, {'object': entry})
