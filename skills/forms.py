from django import forms
from django.forms import TextInput, Textarea

from skills.models import Skills


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please write the name of the skill!', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter a description!', 'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        get_name = cleaned_data.get('name')
        all_skills = Skills.objects.all()
        for skill in all_skills:
            if get_name == skill.name:
                msg = 'There si already a skill with this name added in our database!'
                self._errors['name'] = self.error_class([msg])

        return cleaned_data


class SkillsUpdateForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please write the name of the skill!', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter a description!', 'class': 'form-control'})
        }
