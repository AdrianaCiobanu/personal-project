from django import forms
from django.forms import TextInput, DateInput, Textarea

from experience.models import Experience


class ExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'start_date', 'end_date', 'description']
        widgets = {
            'job_title': TextInput(attrs={'placeholder': 'Please introduce the job title!', 'class': 'form-control'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': Textarea(attrs={'placeholder': 'Please introduce your description', 'class': 'form-control'})
        }
