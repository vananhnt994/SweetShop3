from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):

    welcomeText = {'welcome': "Welcome to my world!"}
    return render(request,'home/index.html',context= welcomeText)

