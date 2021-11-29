from django import forms
from . import models
from ckeditor.widgets import CKEditorWidget


class NewsForm(forms.ModelForm):
    class Meta:
        model = models.News
        fields = ('title', 'body', 'category', 'image', 'text_full')

