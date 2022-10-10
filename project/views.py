# from django.shortcuts import render
import requests
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from project.filters import ProjectFilter
from project.forms import ProjectForm, ProjectUpdateForm
from project.models import Project


class ProjectCreateView(CreateView, PermissionRequiredMixin):
    template_name = 'project/create_project.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('homepage')
    permission_required = 'project.add_project'


class ProjectListView(ListView):
    template_name = 'project/list_of_projects.html'
    model = Project
    context_object_name = 'all_projects'

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        all_projects = Project.objects.all()
        project_filter = ProjectFilter(self.request.GET, queryset=all_projects)
        all_projects = project_filter.qs
        context['all-projects'] = all_projects
        context['project_filter'] = project_filter

        return context


class ProjectUpdateView(UpdateView, PermissionRequiredMixin):
    template_name = 'project/update_project.html'
    model = Project
    form_class = ProjectUpdateForm
    success_url = reverse_lazy('list_of_projects')
    permission_required = 'project.change_project'


class ProjectDetailsView(DetailView):
    template_name = 'project/details_project.html'
    model = Project
    success_url = reverse_lazy('list_of_projects')


class ProjectDeleteView(DeleteView, PermissionRequiredMixin):
    template_name = 'project/delete_project.html'
    model = Project
    success_url = reverse_lazy('list_of_projects')
    permission_required = 'project.delete_project'


@permission_required('project.delete_project')
def delete_project(request, pk):
    Project.objects.filter(id=pk).delete()
    return redirect('list_of_projects')
