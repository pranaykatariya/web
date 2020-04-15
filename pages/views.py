from django.shortcuts import render, redirect
from .models import Admin_Messages, Secret_Message, Slambook
from accounts.models import User_Credentials
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
        data = User_Credentials.objects.get(username= name)
        ctx ={
            'name' : name,  #profile to be visited
            'username' : authenticated_user,    #authenticated user
            'data' : data
        }
        return render(request, 'pages/profile.html', ctx)
        
    else:
        return redirect('/login')    


@login_required(login_url='/login')
def postslam(request, name):    
    authenticated_user = str(request.user)

    if request.method == 'POST':
        no_saved = request.POST['no_saved']
        nickname = request.POST['nickname']
        color_suits = request.POST['color_suits']
        like = request.POST['like']
        dislike = request.POST['dislike']
        similar_things = request.POST['similar_things']
        sweet_memory = request.POST['sweet_memory']
        relation = request.POST['relation']
        song = request.POST['song']
        advice = request.POST['advice']
        share  = request.POST['share']
        secret  = request.POST['secret']
        crush  = request.POST['crush']

        slambook = Slambook(
        to_username=name, 
        from_username=authenticated_user,
        no_saved = no_saved,
        nickname = nickname,
        color_suits = color_suits,
        like = like,
        dislike = dislike,
        similar_things = similar_things,
        sweet_memory = sweet_memory,
        relation = relation,
        song = song,
        advice = advice,
        share  = share,
        secret = secret,
        crush = crush
        )
        
        slambook.save()        
        return redirect('/profile/'+name+'/writeslam')
    else:
        userdata = User_Credentials.objects.get(username= name)
        ctx ={
            'name' : name,  #profile to be visited
            'userdata': userdata
        }
        return render(request, 'pages/writeslam.html',ctx)        


@login_required(login_url='/login')
def userbio(request, name):    
    authenticated_user = str(request.user)

    if request.method == 'POST':
        obj = User_Credentials.objects.get(username= authenticated_user)
        # obj.field = value
        obj.username = authenticated_user
        obj.about = request.POST['about']
        obj.name = request.POST['firstname']
        obj.lastname = request.POST['lastname']
        obj.birthdate = request.POST['birthdate']
        obj.gender = request.POST['gender']
        obj.occupation = request.POST['occupation']
        obj.company = request.POST['company']
        obj.mobile = request.POST['mobile']
        obj.email = request.POST['email']
        obj.insta_username = request.POST['insta_username']
        obj.achievement = request.POST['achievement']
        obj.risk = request.POST['risk']
        obj.happy = request.POST['happy']
        obj.rule = request.POST['rule']
        obj.fear = request.POST['fear']
        obj.evening = request.POST['evening']
        obj.bed = request.POST['bed']
        obj.job = request.POST['job']
        obj.distract = request.POST['distract']
        obj.wish = request.POST['wish']
        obj.save()
        return redirect('/profile/'+authenticated_user+'/userbio')
    else:
        if authenticated_user == name:

            # datasource_sent  = Secret_Message.objects.filter(from_username=authenticated_user)
            # datasource_received = Secret_Message.objects.filter(to_username=authenticated_user)
            data = User_Credentials.objects.get(username= authenticated_user)
            
            ctx ={
                'name' : name,  #profile to be visited
                'data' : data
                # 'datasource_sent': datasource_sent,
                # 'datasource_received': datasource_received
            }
            return render(request,'pages/userbio.html',ctx)
        else:
            return redirect('/profile/'+authenticated_user+'/userbio')
     

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

@login_required(login_url='/login')
def slambook_page(request, name):
    authenticated_user = str(request.user)

    if authenticated_user == name:
        slams = Slambook.objects.filter(to_username= authenticated_user)
        
        # userdata = User_Credentials.objects.filter(username= slams.from_username)

        ctx ={
            'name' : name,  #profile to be visited
            'slams': slams
            # 'userdata': userdata
        }
        return render(request, 'pages/slambook.html',ctx)            
    else:
        return redirect('/profile/'+authenticated_user+'/slambook')    


@login_required(login_url='/login')
def slamprivacy(request, name):
    authenticated_user = str(request.user)
    url=""
    if authenticated_user == name:
        if request.method == 'POST':
            url = request.POST['url']
            id = request.POST['id']
            privacy = request.POST['privacy']
            
            if eval(privacy):
                Slambook.objects.filter(id=id).update(privacy=False)
                print("Public")
            else:
                Slambook.objects.filter(id=id).update(privacy=True)
                print("private")    
            
            return redirect(url+'#'+id)
    else:
        return redirect(url)


def error_page(request, exception):    
    return render(request, 'pages/error.html')        