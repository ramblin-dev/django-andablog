from django.contrib import admin

from .models import Entry


class EntryAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'is_published',
        'published_timestamp',
    )
    search_fields = (
        'title',
        'content',
    )
    readonly_fields = (
        'slug',
        'published_timestamp',
    )

admin.site.register(Entry, EntryAdmin)
