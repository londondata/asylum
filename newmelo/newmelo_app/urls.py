from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns =[
    path('', views.hq, name='hq'),
    path('switchboard', views.switchboard, name='switchboard'),
    path('journal', views.journal, name='journal'),
    path('about', views.about, name='about'),
    path('userlist', views.userlist, name='userlist'),
    path('users/<int:pk>', views.getuser, name='getuser'),
    path('allentries', views.allentries, name='allentries'),
    path('newentry', views.newentry, name='newentry'),
    path('editentry/<int:pk>', views.editentry, name='editentry'),
    path('deleteentry/<int:pk>', views.deleteentry, name='deleteentry'),
    path('entry/<int:pk>', views.findentry, name='findentry'),
    path('entrydetail/<int:pk>', views.entrydetail, name='entrydetail'),
    path('profile/create/<int:pk>', views.createprofile, name='createprofile'),
    path('profile/edit/<int:pk>', views.editprofile, name='editprofile'),
    # path('profile/<int:pk>', views.viewprofile, name='viewprofile'),
    # url(r'^new$', views.createuser, name='createuser'),
]
