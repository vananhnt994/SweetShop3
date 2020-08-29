from django.shortcuts import render
from userapp.models import User
from django.http import HttpResponse
from userapp import forms

# Create your views here.

def sign_up(request):
    form = forms.FormSignUp()

    if request.method == 'POST':
        firstname = request.POST.get('firstname','')
        lastname = request.POST.get('lastname','')
        username = request.POST.get('username','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        user = User.objects.create(username=username , password=password)
        form = forms.FormSignUp(request.POST)
        if form.is_valid():
            # Do something code
            print("Validation success!")
            print("Username : "+ form.cleaned_data['username'])
            print("Email : "+ form.cleaned_data['email'])
            print("Password : "+ form.cleaned_data['password'])
            print("New User is registered")

    return render(request,'userapp/signup.html', {'form': form})

def sign_in(request):
    form = forms.FormSignIn()
    if request.method == 'POST':
        form = forms.FormSignIn(request.POST)
        
        if form.is_valid():
            # Do something code
            print("Validation success!")
            print("Username : "+ form.cleaned_data['username'])
            print("Email : "+ form.cleaned_data['email'])
            print("Password : "+ form.cleaned_data['password'])
            print("the User" + form.cleaned_data['username'] + "is logged in!")

    return render(request,'userapp/login.html', {'form': form})