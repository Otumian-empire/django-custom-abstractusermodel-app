from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from thisapp.customuseradmin import CustomUserAdmin
from thisapp.models import User

# Register your models here.
admin.site.register(User, CustomUserAdmin)
