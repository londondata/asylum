from django import forms
from django.contrib.auth.models import User
from .models import Entry, Gspot, Profile

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'avatar')

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('id', 'title', 'body')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'picture', 'quote', 'birthday', 'disposition', 'location', 'sex')

class GspotForm(forms.ModelForm):
    class Meta:
        model = Gspot
        fields = ('gspot', 'entry')
