from django.conf.urls import url
from userapp import views

# Create your views here.

urlpatterns = [
    url('signup',views.sign_up,name='signup')
]