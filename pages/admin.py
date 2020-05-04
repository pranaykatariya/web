from django.contrib import admin
from .models import Admin_Messages, Secret_Message, Slambook, Promotion_Email_List
# Register your models here.

admin.site.register(Promotion_Email_List)
admin.site.register(Admin_Messages)
admin.site.register(Secret_Message)
admin.site.register(Slambook)