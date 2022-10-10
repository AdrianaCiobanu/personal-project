import django_filters

from project.models import Project


class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Project
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(ProjectFilter, self).__init__(*args, **kwargs)

        self.filters['name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter the name of the project'})
        self.filters['description'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter some description'})
