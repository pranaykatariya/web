from django.db import models

# Create your models here.

class User_Credentials(models.Model):
    name = models.CharField(max_length=64)    
    email = models.EmailField(null=False)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

