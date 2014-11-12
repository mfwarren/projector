from django.shortcuts import render
from django.core.urlresolvers import reverse

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import ListView

from guardian.shortcuts import get_objects_for_user
from guardian.shortcuts import assign_perm

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

from django.http import HttpResponse
from main.models import Project
from .forms import ProjectForm


class ProjectListView(ListView):
    model = Project

    def get_queryset(self, *args, **kwargs):
        return get_objects_for_user(self.request.user, ['main.owns_project', 'main.estimate_project', 'main.view_project'], any_perm=True)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    # These next two lines tell the view to index lookups by username
    # slug_field = "name"
    # slug_url_kwarg = "name"

    def get_queryset(self):
        return get_objects_for_user(self.request.user, ['main.owns_project', 'main.estimate_project', 'main.view_project'], any_perm=True)


class ProjectCreateView(LoginRequiredMixin, CreateView):

    form_class = ProjectForm

    # we already imported User in the view code above, remember?
    model = Project

    def form_valid(self, form):
        form.instance.user = self.request.user
        resp = super(ProjectCreateView, self).form_valid(form)
        if form.instance.pk:
            assign_perm('owns_project', self.request.user, form.instance)
        return resp

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("main:project_detail",
                       kwargs={"pk": self.object.pk})

    def get_object(self):
        # Only get the User record for the user making the request
        return Project.objects.get(pk=self.object.pk)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):

    form_class = ProjectForm

    # we already imported User in the view code above, remember?
    model = Project

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("main:project_detail",
                       kwargs={"pk": self.object.pk})

    def get_object(self):
        # Only get the User record for the user making the request
        p = Project.objects.get(pk=self.object.pk)
        if self.request.user.has_perm('main.owns_project', p):
            return p
        return None
