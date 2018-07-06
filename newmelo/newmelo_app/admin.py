from django.contrib import admin

from .models import User
from .models import Post
from .models import Gspot
from .models import Profile

admin.site.register(User)
admin.site.register(Post)
# Register your models here.
