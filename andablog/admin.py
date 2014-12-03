from django.contrib import admin
from django.db.models import Q
from django.contrib.auth import get_user_model

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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = get_user_model().objects.filter(
                Q(is_superuser=True) | Q(user_permissions__content_type__app_label='andablog',
                                         user_permissions__content_type__model='entry')).distinct()
            kwargs['initial'] = request.user.id
        return super(EntryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class EntryImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entry, EntryAdmin)
admin.site.register(EntryImage, EntryImageAdmin)
