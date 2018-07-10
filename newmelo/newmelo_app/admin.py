from django.contrib import admin

# from .models import User
from .models import Entry
from .models import Gspot
from .models import Profile

# Register your models here.
# admin.site.register(User)
admin.site.register(Entry)
admin.site.register(Gspot)
admin.site.register(Profile)
