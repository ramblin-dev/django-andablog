from . import models
from . import forms


def get_model():
    return models.DemoComment


def get_form():
    return forms.DemoCommentForm
