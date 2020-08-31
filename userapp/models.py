from django.db import models

# Create your models here.

class User(models.Model):

    username = models.CharField(max_length=255,unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255,unique=True)
    verify_password = models.CharField(max_length=255)

    def __str__(self):
        return str(self.username)
