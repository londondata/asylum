from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns =[
    path('', views.main, name='main'),
    url(r'^users$', views.userlist, name='userlist'),
    url(r'users/(?P<pk>\d+)$', views.getuser, name='getuser'),
    url(r'^new$', views.createuser, name='createuser'),
    url(r'^all$', views.allentries, name='allentries'),
    url(r'^newentry$', views.newentry, name='newentry'),
    # path('/newentry', views.newentry, name='newentry'),
    url(r'^editentry/(?P<pk>\d+)$', views.editentry, name='editentry'),
    url(r'^deleteentry/(?P<pk>\d+)$', views.deleteentry, name='deleteentry'),
    url(r'^profile$', views.createprofile, name='createprofile'),
    url(r'^edit/(?P<pk>\d+)$', views.editprofile, name='editprofile'),
]