from django.contrib import admin
from base.models import UserProfile
from .models import MyModel

# Register your models here.
admin.site.register(UserProfile)

admin.site.register(MyModel)