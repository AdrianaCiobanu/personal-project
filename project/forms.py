from django import forms
from django.forms import TextInput, Textarea

from project.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please write the name of the project!', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please describe the project!', 'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        get_name = cleaned_data.get('name')
        get_description = cleaned_data.get('description')
        all_projects = Project.objects.all()
        for project in all_projects:
            if get_name == project.name and get_description == project.description:
                msg = 'There is already a project with this name in our data base!'
                self._errors['name'] = self.error_class([msg])

        return cleaned_data


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please write the name of the project!', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please describe the project!', 'class': 'form-control'})
        }


