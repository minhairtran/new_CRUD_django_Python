from django.contrib import admin
from django.urls import path

from Student.views import (
    StudentDetailView,
    StudentListView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
)

app_name = 'Student'
urlpatterns = [
    path('all/', StudentListView.as_view(), name='student-list'),
    path('<int:id>/', StudentDetailView.as_view(), name='student-detail'),
    path('<int:id>/update', StudentUpdateView.as_view(), name='student-update'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('<int:id>/delete', StudentDeleteView.as_view(), name='student-delete'),
]