import six
from django.db import models

from authtools.models import AbstractEmailUser
from django.template.defaultfilters import slugify


class User(AbstractEmailUser):
    name = models.CharField(max_length=100)
    profile_name = models.CharField('profile name', max_length=20, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    REQUIRED_FIELDS = ['name', 'profile_name']  # Base already includes email

    def save(self, *args, **kwargs):
        self.slug = slugify(self.profile_name)
        super(User, self).save()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        """Required by And-a-Blog for displaying author of a (blog/comment)"""
        return self.profile_name

    def get_absolute_url(self):
        """Since it's provided And-a-Blog will use this to link to an author's profile"""
        return self.userprofile.get_absolute_url()

    def __unicode__(self):
        return six.text_type(self.get_short_name())
