from django.db import models
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, help_text="enter your username - choose wisely!")
    user_id = models.IntegerField()
    avatar = models.TextField()
    password = models.TextField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    picture = models.TextField()
    name = models.CharField(max_length=150)
    quote = models.TextField()
    birthday = models.DateField()
    disposition = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.TextField()
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True, related_name='username')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Gspot(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null = True, blank = True, related_name='postname')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
