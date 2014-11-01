from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='authordisplay')
def author_display(author, *args):
    """Returns either the linked or not-linked profile name."""

    # Call get_absolute_url or a function returning none if not defined
    url = getattr(author, 'get_absolute_url', lambda: None)()
    # get_short_name is not optional (to andablog) so we use what we  get
    short_name = author.get_short_name()
    if url:
        return mark_safe('<a href="{}">{}</a>'.format(url, short_name))
    else:
        return short_name
