from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from resume.forms import ResumeUpdateForm
from resume.models import Resume


class ResumeListView(ListView):
    template_name = 'resume/list_resume.html'
    model = Resume
    context_object_name = 'all_resumes'

    def get_context_data(self, **kwargs):
        context = super(ResumeListView, self).get_context_data(**kwargs)
        all_resumes = Resume.objects.all()
        context['all-resumes'] = all_resumes

        return context


class ResumeUpdateView(UpdateView):
    template_name = 'resume/update_resume.html'
    model = Resume
    form_class = ResumeUpdateForm
    success_url = reverse_lazy('list_resume')


class ResumeDeleteView(DeleteView):
    template_name = 'resume/delete_resume.html'
    model = Resume
    success_url = reverse_lazy('list_resume')


def delete_resume(request, pk):
    Resume.objects.filter(id=pk).delete()
    return redirect('list_resume')
