from django.db import models

# Create your models here.

class Promotion_Email_List(models.Model):
    email = models.EmailField(null=False, unique=True)
    sent = models.BooleanField(default=False)


class Admin_Messages(models.Model):
    name = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    email = models.EmailField(null=False)
    message = models.TextField(null=True, blank=True)


class Secret_Message(models.Model):
    to_username = models.CharField(max_length=64)    
    from_username = models.CharField(max_length=64)
    message = models.TextField()
    timestamp_message = models.DateTimeField(auto_now_add=True)


class Slambook(models.Model):
    to_username = models.CharField(max_length=64)    
    from_username = models.CharField(max_length=64)
    no_saved = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64)
    color_suits = models.CharField(max_length=128)
    like = models.TextField()
    dislike = models.TextField()
    similar_things = models.TextField()
    sweet_memory = models.TextField()
    relation = models.CharField(max_length=64)
    song = models.TextField()
    advice = models.TextField()
    secret = models.TextField()
    crush = models.TextField()
    privacy = models.BooleanField(default=True)
    share  = models.CharField(max_length=64)
    timestamp_slam = models.DateTimeField(auto_now_add=True)