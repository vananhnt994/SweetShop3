from django.db import models
#from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager,PermissionsMixin

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, username, password, alias=None):
#         if not email:
#             raise ValueError("ENTER AN EMAIL BUDDY")
#         if not username:
#             raise ValueError("I KNOW YOU HAVE A NAME")
#         if not password:
#             raise ValueError("PASSWORD?!?!?!? HELLO??")
#         if not alias:
#             alias = username
        
#         user = self.model(
#              email = self.normalize_email(email),
#              username = username,
#              alias = alias)
#         user.set_password(password)
#         user.save()
#         return user
#     def create_superuser(self, email, username, password, alias=None):
#         user = self.create_user(email, username, password, alias)
#         user.is_staff()
#         user.is_superuser = True
#         user.save()
#         return user
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):

    username = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to="user_data/profile_picture", blank=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=10, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255,unique=True)

    is_staff=models.BooleanField(default=False)
    last_login =  models.DateTimeField( blank=True, null=True)
    is_active = models.BooleanField(default=True)
    verify_password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)
    #     self._password = raw_password

    def __str__(self):
        return self.get_username()
    objects = UserManager()
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    portfolio_site = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

