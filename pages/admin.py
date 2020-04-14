from django.contrib import admin
from .models import Admin_Messages, Secret_Message, Slambook
# Register your models here.

admin.site.register(Admin_Messages)
admin.site.register(Secret_Message)
admin.site.register(Slambook)