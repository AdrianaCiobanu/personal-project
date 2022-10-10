from django import forms
from django.forms import TextInput, EmailInput, Textarea

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Your name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Your email', 'class': 'form-control'}),
            'phone': TextInput(attrs={'placeholder': 'Your phone', 'class': 'form-control'}),
            'message': Textarea(attrs={'placeholder': 'Your message', 'class': 'form-control'})
        }

