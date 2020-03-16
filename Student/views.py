from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import StudentModelForm, StudentCreateForm
from Student.models import Student
from django.urls import reverse

class StudentDetailView(DetailView):
    template_name = 'Student/student_detail_view.html'
    queryset = Student.objects.all()

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Student, id=id)

class StudentListView(ListView):
    template_name = "Student/student_list_view.html"
    queryset = Student.objects.all()

class StudentCreateView(CreateView):
   template_name = "Student/student_create_view.html"
   form_class = StudentModelForm
   queryset = Student.objects.all()
    

class StudentUpdateView(UpdateView):
    template_name = "Student/student_update_view.html"
    queryset = Student.objects.all()
    form_class = StudentModelForm

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Student, id=id)

class StudentDeleteView(DeleteView):
    template_name = "Student/student_delete_view.html"
    queryset = Student.objects.all()

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Student, id=id)

    def get_success_url(self):
        return reverse('Student:student-list')