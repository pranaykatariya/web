from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import auth, messages
from django.views.decorators.http import require_GET
from .models import User_Credentials
import sys

#Create your views here.


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow:",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def logout(request):
    auth.logout(request)
    return redirect('/')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/profile/'+str(request.user))
    else:        
        if request.method == 'POST':        
            user = request.POST['username']
            password = request.POST['password1']
            
            user = auth.authenticate(username= user, password= password)

            if user is not None:
                auth.login(request,user)
                return redirect('/profile/'+str(request.user))
            else:
                messages.info(request,'Invalid credentials')
                return redirect('/login')     
        else:
            return render(request, 'accounts/login.html')
    

def signup_page(request):    
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            user = request.POST.get('username')
            password = request.POST.get('password1')
            user.split()
            try:
                user = User.objects.create_user(username=user, email=email, password= password, first_name = name)
                user.save()
                client = User_Credentials(name=name,email=email,username=user,password=password)
                client.save()
                return redirect('/login')
            except:
                messages.info(request,'Username taken!!!')
                print('username taken')
                # print(sys.exc_info()[0])
                return redirect('/signup')
        else:
            return render(request, 'accounts/signup.html')    