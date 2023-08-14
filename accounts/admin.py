from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import ChatUser
# Register your models here.
class ChatUserAdmin(UserAdmin):
    list_display = ("username", 'is_admin', 'is_staff')
    search_fields = 'username',
    readonly_fields = 'id',

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(ChatUser, ChatUserAdmin)
admin.site.unregister(Group)