from django.contrib import admin

from .models import DemoComment


class DemoCommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'submit_date',
    )
    search_fields = (
        'user__profile_name',
        'user__email',
        'comment',
    )

admin.site.register(DemoComment, DemoCommentAdmin)
