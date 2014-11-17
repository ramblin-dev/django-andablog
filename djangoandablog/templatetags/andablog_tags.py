from django import template
from django.utils.safestring import mark_safe
import six

register = template.Library()


@register.filter(name='authordisplay')
def author_display(author, *args):
    """Returns either the linked or not-linked profile name."""

    # Call get_absolute_url or a function returning none if not defined
    url = getattr(author, 'get_absolute_url', lambda: None)()
    # get_short_name or unicode representation
    short_name = getattr(author, 'get_short_name', lambda: six.text_type(author))()
    if url:
        return mark_safe('<a href="{}">{}</a>'.format(url, short_name))
    else:
        return short_name
