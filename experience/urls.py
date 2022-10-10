from django.urls import path

from experience import views

urlpatterns = [
    path('list-of-experiences/', views.ExperienceListView.as_view(), name='list_of_experiences'),
    path('update-experience/<int:pk>', views.ExperienceUpdateView.as_view(), name='update_experience'),
    path('details-experience/<int:pk>', views.ExperienceDetailsView.as_view(), name='details_experience'),
    path('delete-experience/<int:pk>', views.ExperienceDeleteView.as_view(), name='delete_experience'),
]
