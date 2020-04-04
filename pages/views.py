from django.shortcuts import render, redirect
from .models import Admin_Messages
from django.contrib import messages

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

def profile_page(request):
    if request.user.is_authenticated:
        return render(request, 'pages/profile.html')
    else:
        return redirect('/login')    
        
def error_page(request, exception):    
    return render(request, 'pages/error.html')        
