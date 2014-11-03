from django.contrib import admin

from .models import Entry, EntryImage


class EntryImageInline(admin.TabularInline):
    model = EntryImage
    extra = 1
    readonly_fields = ['image_url']


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

    inlines = [
        EntryImageInline,
    ]


class EntryImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entry, EntryAdmin)
admin.site.register(EntryImage, EntryImageAdmin)
