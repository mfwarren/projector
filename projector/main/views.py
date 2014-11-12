from django.shortcuts import render
from django.core.urlresolvers import reverse

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

from django.http import HttpResponse
from main.models import Project
from .forms import ProjectForm


class ProjectListView(ListView):
    model = Project

    # def head(self, *args, **kwargs):
    #     last_book = self.get_queryset()
    #     response = HttpResponse('')
    #     # RFC 1123 date format
    #     response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
    #     return response

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    # These next two lines tell the view to index lookups by username
    # slug_field = "name"
    # slug_url_kwarg = "name"

class ProjectUpdateView(LoginRequiredMixin, UpdateView):

    form_class = ProjectForm

    # we already imported User in the view code above, remember?
    model = Project

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("main:project_detail",
                       kwargs={"pk": self.request.project.pk})

    def get_object(self):
        # Only get the User record for the user making the request
        return Project.objects.get(pk=self.request.project.pk)
