from django.contrib import admin
from userapp.models import User,UserProfileInfo
# Register your models here.

admin.site.register(User)
admin.site.register(UserProfileInfo)

