import django_comments.models as dmodels


class RelatedCommentManager(dmodels.CommentManager):

    def get_queryset(self):
        return super(RelatedCommentManager, self).get_queryset().select_related(
            'user',
            'user__profile'
        )


class DemoComment(dmodels.Comment):

    class Meta:
        proxy = True
        app_label = 'democomments'

    objects = RelatedCommentManager()
