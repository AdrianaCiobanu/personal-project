# from django.shortcuts import render
# import requests
import requests
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from skills.forms import SkillsForm, SkillsUpdateForm
from skills.models import Skills


class SkillsCreateView(CreateView, PermissionRequiredMixin):
    template_name = 'skills/create_skill.html'
    model = Skills
    form_class = SkillsForm
    success_url = reverse_lazy('list_of_skills')
    permission_required = 'skills.create_skills'


class SkillsListView(ListView):
    template_name = 'skills/list_of_skills.html'
    model = Skills
    context_object_name = 'all_skills'

    def get_context_data(self, **kwargs):
        context = super(SkillsListView, self).get_context_data(**kwargs)
        all_skills = Skills.objects.all()
        context['all-skills'] = all_skills

        return context


class SkillsUpdateView(UpdateView, PermissionRequiredMixin):
    template_name = 'skills/update_skill.html'
    model = Skills
    form_class = SkillsUpdateForm
    success_url = reverse_lazy('list_of_skills')
    permission_required = 'skills.update_skills'


class SkillsDeleteView(DeleteView, PermissionRequiredMixin):
    template_name = 'skills/delete_skill.html'
    model = Skills
    success_url = reverse_lazy('list_of_skills')
    permission_required = 'skills.delete_skills'


@permission_required('skills.delete_skills')
def delete_project(request, pk):
    Skills.objects.filter(id=pk).delete()
    return redirect('list_of_skills')
