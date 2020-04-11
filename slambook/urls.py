"""slambook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404, handler500
from pages import views as pages_views

#from accounts app
from accounts.views import login_page
from accounts.views import signup_page
from accounts.views import logout

# from pages app
from pages.views import about_page
from pages.views import contact_page
from pages.views import home_page
from pages.views import profile_page, postsecretmessage, postslam, secretmessages, userbio, friends_page
from pages.views import error_page



urlpatterns = [
    path('', home_page, name='home_page'),
    path('home', home_page, name='home_page'),
    path('contact', contact_page, name='contact_page'),
    path('about', about_page, name='about_page'),
    

    path('login', login_page, name='login_page'),
    path('signup', signup_page, name='signup_page'),
    path('logout', logout, name='logout'),

    path('profile/<str:name>', profile_page, name='profile_page'),
    path('profile/<str:name>/writeslam', postslam, name='postslam'),
    path('profile/<str:name>/writesecretmessage', postsecretmessage, name='postsecretmessage'),
    path('profile/<str:name>/secretmessages', secretmessages, name='secretmessages'),
    path('profile/<str:name>/userbio', userbio, name='userbio'),
    path('profile/<str:name>/friends', friends_page, name='friends_page'),


    path('admin/', admin.site.urls),

]

handler404 = pages_views.error_page
