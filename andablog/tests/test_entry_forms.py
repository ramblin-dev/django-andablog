from django.forms import ModelForm
from django.test import TestCase

from andablog import models


class TestEntryEditing(TestCase):

    def setUp(self):
        self.entry = models.Entry.objects.create(title=u'Welcome!', content='### Some Content', is_published=False)

        class EntryForm(ModelForm):
            class Meta:
                model = models.Entry
                fields = ['title', 'content', 'is_published']

        self.form_cls = EntryForm

    def test_form_editing(self):
        """Should be able to properly edit an entry within a model form"""
        update = {
            'title': 'Last Post (Final)',
            'content': '### Goodbye!',
            'is_published': True,
        }

        form = self.form_cls(update, instance=self.entry)

        form.save()

        actual = models.Entry.objects.get(pk=self.entry.pk)
        self.assertEquals(actual.title, update['title'])
        self.assertEquals(actual.content.raw, update['content'])
        self.assertIsNotNone(actual.published_timestamp)


class TestEntryCreation(TestCase):

    def setUp(self):
        class EntryForm(ModelForm):
            class Meta:
                model = models.Entry
                fields = ['title', 'content', 'is_published']

        self.form_cls = EntryForm

    def test_form_create(self):
        """Should be able to properly create an entry within a model form"""
        create = {
            'title': 'Last Post (Final)',
            'content': '### Goodbye!',
            'is_published': False,
        }

        form = self.form_cls(create)
        print(form.errors)

        form.save()

        actual = models.Entry.objects.get(slug='last-post-final')
        self.assertEquals(actual.title, create['title'])
        self.assertEquals(actual.content.raw, create['content'])
        self.assertIsNone(actual.published_timestamp)
