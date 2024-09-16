from django import forms
from .models import Task, Photo


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'is_complete']
        widgets = {
            'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
