"""djproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from book.views import home_view,user_login,user_logout,register,adminlogin,sellbook,delete,verify,buybook,buy,userchoice,dash_board

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name='home'),
    path('adminlogin/',adminlogin),
    path('sellbook/',sellbook),
    path('buybook/',buybook),
    path('buy/<id>',buy),
    path('delete/',delete),
    path('verify/',verify),
    path('dashboard/',dash_board),
    path('userchoice/',userchoice),
    #path('delete-book/<id>',deletebook),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('register/',register, name='register'),

]
