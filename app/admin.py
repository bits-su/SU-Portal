from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


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

admin.site.register(User, UserAdmin)
