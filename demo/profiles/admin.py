from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'greatest_fear',
    )
    search_fields = (
        'user__email',
        'user__name',
        'user__profile_name',
        'user__slug',
        'greatest_fear',
        'home',
    )

admin.site.register(UserProfile, UserProfileAdmin)
