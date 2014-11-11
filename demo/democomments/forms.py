from django_comments.forms import CommentForm
from django import forms

from .models import DemoComment


class DemoCommentForm(CommentForm):

    def __init__(self, *args, **kwargs):
        super(DemoCommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.Textarea(attrs={'rows': 2})

    def get_comment_model(self):
        return DemoComment
