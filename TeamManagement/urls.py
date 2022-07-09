from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-member/', views.add_member, name='add-member'),
    path('edit-member/<int:pk>', views.edit_member, name='edit-member'),
]
