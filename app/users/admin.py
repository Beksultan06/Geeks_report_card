from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'role', 'direction')

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    list_display = ['id', 'username', 'role']
    list_filter = ['role']
    search_fields = ['id', 'username', 'role']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'first_name', 'last_name', 'role', 'direction')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'role', 'direction'),
        }),
    )
