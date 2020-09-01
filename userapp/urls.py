from django.conf.urls import url
from userapp import views

# Create your views here.
app_name ='userapp'
urlpatterns = [
    url('signup',views.sign_up,name='signup'),
    url('login',views.sign_in,name='signin')
]