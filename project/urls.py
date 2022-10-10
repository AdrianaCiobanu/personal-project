from django.urls import path

from project import views

urlpatterns = [
    path('create-project/', views.ProjectCreateView.as_view(), name='create_project'),
    path('list-of-projects/', views.ProjectListView.as_view(), name='list_of_projects'),
    path('update-project/<int:pk>', views.ProjectUpdateView.as_view(), name='update_project'),
    path('details-project/<int:pk>', views.ProjectDetailsView.as_view(), name='details_project'),
    path('delete-project/<int:pk>', views.ProjectDeleteView.as_view(), name='delete_project'),
]
