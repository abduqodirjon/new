from django import forms
from . import models
from ckeditor.widgets import CKEditorWidget
class NewsForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.News
        fields = ('title', 'content', 'category', 'image', 'text_full')