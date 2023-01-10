from django.contrib import admin
from .models import (
    User,
    Profile
)


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email", "phone_number",)

# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Profile)