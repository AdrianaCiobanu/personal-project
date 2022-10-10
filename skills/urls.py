from django.urls import path

from skills import views

urlpatterns = [
    path('create-skill/', views.SkillsCreateView.as_view(), name='create_skill'),
    path('list-of-skills/', views.SkillsListView.as_view(), name='list_of_skills'),
    path('update-skill/<int:pk>', views.SkillsUpdateView.as_view(), name='update_skill'),
    path('delete-skill/<int:pk>', views.SkillsDeleteView.as_view(), name='delete_skill')
]
