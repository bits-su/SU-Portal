from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Complaint


class UserAdmin(UserAdmin):

    fieldsets = [
        (None, {
            'fields': ['username', 'password']
            }),
        ('Personal info', {
            'fields': ['first_name', 'last_name', 'phone', 'email', 'image']
            }),
        ('Permissions', {
            'fields': ['is_active', 'is_staff', 'is_superuser',]
            }),
    ]

class ComplaintAdmin(admin.ModelAdmin):

    list_display = [
        'complaint_id',
        'title',
        'complaint',
        'uploadedby',
    ]

    list_display_links = [
        'complaint_id',
        'title',
        'complaint',
    ]

admin.site.register(User, UserAdmin)
admin.site.register(Complaint, ComplaintAdmin)
