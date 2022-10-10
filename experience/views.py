# from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView

from experience.forms import ExperienceUpdateForm
from experience.models import Experience


class ExperienceListView(ListView):
    template_name = 'experience/list_of_experiences.html'
    model = Experience
    context_object_name = 'all_experiences'

    def get_context_data(self, **kwargs):
        context = super(ExperienceListView, self).get_context_data(**kwargs)
        all_experiences = Experience.objects.all()
        context['all-experiences'] = all_experiences

        return context


class ExperienceUpdateView(UpdateView, PermissionRequiredMixin):
    template_name = 'experience/update_experience.html'
    model = Experience
    form_class = ExperienceUpdateForm
    success_url = reverse_lazy('list_of_experiences')
    permission_required = 'experience.change_experience'


class ExperienceDeleteView(DeleteView, PermissionRequiredMixin):
    template_name = 'experience/delete_experience.html'
    model = Experience
    success_url = reverse_lazy('list_of_experiences')
    permission_required = 'experience.delete_experience'


@permission_required('experience.delete_experience')
def delete_experience(request, pk):
    Experience.objects.filter(id=pk).delete()
    return redirect('list_of_experiences')


class ExperienceDetailsView(DetailView):
    template_name = 'experience/details_experience.html'
    model = Experience
    success_url = reverse_lazy('list_of_experiences')

