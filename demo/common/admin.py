from django.contrib import admin

from authtools.admin import UserAdmin

from .models import User

admin.site.register(User, UserAdmin)
