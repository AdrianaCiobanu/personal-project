from django import forms
from django.forms import TextInput

from resume.models import Resume


class ResumeUpdateForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please add the updated resume!', 'class': 'form-control'})
        }
