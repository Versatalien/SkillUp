from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Courses
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

#mixins
class OwnerMixin(object):
    def get_queryset(self): 
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user) 
    
class OwnerEditMixin(object): 
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class OwnerCourseMixin(OwnerMixin,LoginRequiredMixin,PermissionRequiredMixin): 
    model = Courses
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')
    
class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = 'courses/manage/course/form.html'
    

# Create your views here.

class ManageCourseListView(ListView): 
    model = Courses
    template_name = 'courses/manage/course/list.html'
    permission_required = 'courses.view_courses'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
    
    
class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_courses'

class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required = 'courses.change_courses'

class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'
    permission_required = 'courses.delete_courses'
    
    
    
    