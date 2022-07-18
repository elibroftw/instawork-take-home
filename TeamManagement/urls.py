from django.urls import path

from . import views

app_name = 'TeamManagement'

urlpatterns = [
    path('', views.TeamMemberListView.as_view(), name='index'),
    path('add-member/', views.add_member, name='add-member'),
    path('edit-member/<int:pk>', views.edit_member, name='edit-member'),
]
