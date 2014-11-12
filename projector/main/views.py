from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

from django.http import HttpResponse
from main.models import Project


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
