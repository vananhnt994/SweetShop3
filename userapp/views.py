from django.shortcuts import render , redirect
from userapp.models import User,UserProfileInfo
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from userapp import forms
from django.views.decorators.csrf import csrf_protect , csrf_exempt

# Create your views here.
@csrf_exempt
def sign_up(request):

    registered = False
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            authenticate(request, username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()
    print(user_form.is_valid() , profile_form.is_valid())
    return render(request,'userapp/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

@csrf_exempt
def sign_in(request):

    form = forms.UserProfileInfoForm()
    if request.method == 'POST':
        form = forms.UserProfileInfoForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_staff and user.is_superuser :
                return render(request,'index')
            else:
                return HttpResponseRedirect(reverse('index'))
        
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'userapp/login.html', {})

@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))