from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView

from . import models


class UserProfileDetail(DetailView):
    model = models.UserProfile
    context_object_name = 'profile'
    slug_field = 'user__slug'


def profile_redirect(request):
    if request.user.is_authenticated():
        url = reverse('profile-detail', args=[str(request.user.slug)])
        return HttpResponseRedirect(url)
