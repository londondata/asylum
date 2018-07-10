from django.db import models
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, help_text="enter your username - choose wisely!")
    user_id = models.IntegerField()
    avatar = models.TextField()
    password = models.TextField(max_length=100)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True, related_name='profile')

    def __str__(self):
        return self.name

class Entry(models.Model):
    title = models.TextField()
    body = models.TextField()
    tag = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True, related_name='entry')
    # created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Gspot(models.Model):
    gspot = models.TextField()
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, null = True, blank = True, related_name='gspot')
    # created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
