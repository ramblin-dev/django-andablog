"""
NOTE: Can not import models at module level because all app model loading must first be finished.
"""

def get_model():
    from . import models
    return models.DemoComment


def get_form():
    from . import forms
    return forms.DemoCommentForm
