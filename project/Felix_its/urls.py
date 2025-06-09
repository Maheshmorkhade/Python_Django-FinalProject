from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_felix, name='all_felix'),
    path('create/', views.create_course, name='create_course'),
    path('update/<int:pk>/', views.update_course, name='update_course'),
    path('delete/<int:pk>/', views.delete_course, name='delete_course'),
]
