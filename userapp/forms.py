from django import forms
from django.core import validators
from django.forms import ModelForm
from userapp.models import User , UserProfileInfo

# class FormSignUp(forms.ModelForm):
#     class Meta:  
#         model = User
#         fields = ['username','firstname','lastname','email','password','verify_password']
#         widgets = {
#         'password': forms.PasswordInput(),
#         'verify_password' :forms.PasswordInput(),
#         'email': forms.EmailInput
#     }
  
#     # username = forms.CharField(max_length=255)
#     # firstname = forms.CharField(max_length=255)
#     # lastname = forms.CharField(max_length=255)
#     # email = forms.EmailField(max_length=13)
#     # password = forms.CharField(widget=forms.PasswordInput)
#     # verify_password = forms.EmailField(label="Enter your password again!")
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if User.objects.filter(username__iexact=username).exists():
#             raise forms.ValidationError('Username already exists')
#         return username
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if User.objects.filter(email__iexact=email).exists():
#             raise forms.ValidationError('A user has already registered using this email')
#         return email

#     def clean_password(self):
         
#          password = self.cleaned_data.get('password')
#          vpass = self.cleaned_data.get('verify_password')
#          if password != vpass:
#             raise forms.ValidationError("Make sure password match!")
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class FormSignIn(forms.Form):

    username = forms.CharField(max_length=255)
    #email = forms.EmailField(max_length=13)
    password = forms.CharField(widget=forms.PasswordInput)

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')
    