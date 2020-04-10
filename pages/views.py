from django.shortcuts import render, redirect
from .models import Admin_Messages, Secret_Message
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def about_page(request):
    return render(request, 'pages/about.html')

def contact_page(request):    
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        mess = request.POST['message']
        msg = Admin_Messages(name=name,subject=subject,email=email,message=mess)
        msg.save()
        messages.info(request,'Thanks for your valuable feedback. <br> We will get back to you soon.')
        return redirect('/contact')
    else:    
        return render(request, 'pages/contact.html')    

def home_page(request):    
    return render(request, 'pages/home.html')

@login_required(login_url='/login')
def profile_page(request, name):
    if request.user.is_authenticated:
        
        authenticated_user = str(request.user)
        
        ctx ={
            'name' : name,  #profile to be visited
            'user' : authenticated_user    #authenticated user
        }
        
        return render(request, 'pages/profile.html', ctx)
    else:
        return redirect('/login')    
        

def postslam(request, name):    
    return render(request, 'pages/writeslam.html')        


def userbio(request, name):    
    return render(request, 'pages/userbio.html')        



@login_required(login_url='/login')
def secretmessages(request, name):    
    authenticated_user = str(request.user)

    if authenticated_user == name:
        datasource_sent  = Secret_Message.objects.filter(from_username=authenticated_user)
        datasource_received = Secret_Message.objects.filter(to_username=authenticated_user)
        ctx ={
            'name' : name,  #profile to be visited
            'datasource_sent': datasource_sent,
            'datasource_received': datasource_received
        }
        return render(request,'pages/secretmessages.html',ctx)
    else:
        return redirect('/profile/'+authenticated_user+'/secretmessages')
        



@login_required(login_url='/login')
def postsecretmessage(request, name):    
    authenticated_user = str(request.user)

    if request.method == 'POST':
        mess = request.POST['message']
        secret_msg = Secret_Message(to_username=name, from_username=authenticated_user,message= mess)
        secret_msg.save()        
        return redirect('/profile/'+name+'/writesecretmessage')
    else:
        list  = Secret_Message.objects.filter(to_username=name, from_username=authenticated_user)
        ctx ={
            'name' : name,  #profile to be visited
            'datasource': list
        }
        return render(request, 'pages/writesecretmessage.html',ctx)            


def error_page(request, exception):    
    return render(request, 'pages/error.html')        
