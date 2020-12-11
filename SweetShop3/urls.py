"""SweetShop3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from userapp import views as user
from home import views as home
from product_catalog import views as product
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.index,name="index"),
    path('signup/',user.sign_up,name="signup"),
    path('logout/',user.user_logout,name="logout"),
    path('special/',user.special,name='special'),
    path('userapp/',include('userapp.urls')),
    path('login/',user.sign_in,name="login"),
    path('drinks/',product.ProductListView.drink_list,name='drink_list'),
    path('cakes/',product.ProductListView.cake_list,name='cake_list')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)