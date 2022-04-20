from django.contrib import admin
from app_users.models import UserProfileInfo, Contact
# Register your models here.
admin.site.register(UserProfileInfo)

class ContactToAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','feedback')

admin.site.register(Contact, ContactToAdmin)