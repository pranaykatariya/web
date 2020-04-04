from django.db import models

# Create your models here.

class Admin_Messages(models.Model):
    name = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    email = models.EmailField(null=False)
    message = models.TextField(null=True, blank=True)


