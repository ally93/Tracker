# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"

    def get_queryset(self):
        return Project.objects.filter(members__in=[self.request.user.id])

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"

