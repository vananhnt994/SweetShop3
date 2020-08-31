from django.shortcuts import render , redirect
from userapp.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from userapp import forms
from django.views.decorators.csrf import csrf_protect , csrf_exempt

# Create your views here.
@csrf_exempt
def sign_up(request):
    form = forms.FormSignUp()

    if request.method == 'POST':
        firstname = request.POST.get('firstname','')
        lastname = request.POST.get('lastname','')
        username = request.POST.get('username','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        verify_password = request.POST.get('verify_password','')
        
        user = User.objects.create(username=username , password=password, verify_password = verify_password,email = email,firstname=firstname,lastname=lastname)
        form = forms.FormSignUp(request.POST)
        if form.is_valid():
            user.authenticate()
            login(request,user)
            print("Validation success!")
            print("Username : "+ form.cleaned_data['username'])
            print("Email : "+ form.cleaned_data['email'])
            print("Password : "+ form.cleaned_data['password'])
            print("New User is registered")
        
        return redirect('index')

    else:
        form = forms.FormSignUp()

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