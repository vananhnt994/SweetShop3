from django import forms
from django.core import validators
from django.forms import ModelForm
from userapp.models import User

class FormSignUp(forms.ModelForm):
    class Meta:  
        model = User
        fields = ['username','firstname','lastname','email','password','verify_password']
        widgets = {
        'password': forms.PasswordInput(),
        'verify_password' :forms.PasswordInput(),
        'email': forms.EmailInput
    }
    # username = forms.CharField(max_length=255)
    # firstname = forms.CharField(max_length=255)
    # lastname = forms.CharField(max_length=255)
    # email = forms.EmailField(max_length=13)
    # password = forms.CharField(widget=forms.PasswordInput)
    # verify_password = forms.EmailField(label="Enter your password again!")

    # def clean(self):
    #     all_clean_data = super().clean()
    #     password = all_clean_data['password']
    #     vpass = all_clean_data['verify_password']
    #     if password != vpass:
    #         raise forms.ValidationError("Make sure emails match!")
    

class FormSignIn(forms.Form):

    username = forms.CharField(max_length=255)
    #email = forms.EmailField(max_length=13)
    password = forms.CharField(widget=forms.PasswordInput)
    