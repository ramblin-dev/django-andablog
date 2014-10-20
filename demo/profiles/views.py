from django.views.generic import DetailView

from . import models


class UserProfileDetail(DetailView):
    model = models.UserProfile
    context_object_name = 'profile'
    slug_field = 'user__slug'
