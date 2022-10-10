from django.urls import path

from resume import views

urlpatterns = [
    path('list-resume/', views.ResumeListView.as_view(), name='list_resume'),
    path('update-resume/<int:pk>', views.ResumeUpdateView.as_view(), name='update_resume'),
    path('delete-resume/<int:pk>', views.ResumeDeleteView.as_view(), name='delete_resume')

]
