from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'types', 'statuses')

    def clean_tite(self):
        title = self.cleaned_data('title')
        if len(title) < 2:
            raise ValidationError('Title should be longer than 2')
        return title
