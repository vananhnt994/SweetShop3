from django.conf.urls import url
from product_catalog import views

app_name= 'product_catalog'
urlpatterns = [
    url('drink_list',views.drink_list,name='drink_list'),
    url('cake_list',views.cake_list,name='cake_list'),



]
