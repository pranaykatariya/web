from django.db import models

# Create your models here.

class User_Credentials(models.Model):
    
    #personal
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64,null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    email = models.EmailField(null=False)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=12, null=True, blank=True)
    occupation = models.CharField(max_length=250,null=True, blank=True)
    company = models.CharField(max_length=250,null=True, blank=True)
    mobile = models.CharField(max_length=64,null=True, blank=True)
    insta_username = models.CharField(max_length=128,null=True, blank=True)

    #Firsts
    achievement = models.TextField(null=True, blank=True)
    risk = models.TextField(null=True,blank=True)
    happy = models.TextField(null=True, blank=True)
    rule = models.TextField(null=True, blank=True)

    # what
    fear = models.TextField(null=True, blank=True)
    evening = models.TextField(null=True, blank=True)
    bed = models.TextField(null=True, blank=True)
    job = models.TextField(null=True, blank=True)
    distract = models.TextField(null=True, blank=True)
    wish = models.TextField(null=True, blank=True)

