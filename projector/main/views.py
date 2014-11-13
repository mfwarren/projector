from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import ListView

from guardian.shortcuts import get_objects_for_user
from guardian.shortcuts import assign_perm

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

from main.models import Project
from .forms import ProjectForm


class ProjectListView(ListView):
    model = Project

    def get_queryset(self, *args, **kwargs):
        return get_objects_for_user(self.request.user, ['main.owns_project', 'main.estimate_project', 'main.view_project'], any_perm=True)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    # These next two lines tell the view to index lookups by username
    slug_field = "slug"
    slug_url_kwarg = "name"

    def get_queryset(self, *args, **kwargs):
        return get_objects_for_user(self.request.user, ['main.owns_project', 'main.estimate_project', 'main.view_project'], any_perm=True)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        if self.object.pk:
            assign_perm('owns_project', self.request.user, self.object)
        return HttpResponseRedirect(self.get_success_url())

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("main:project_detail",
                       kwargs={"name": self.object.slug})


class ProjectUpdateView(LoginRequiredMixin, UpdateView):

    form_class = ProjectForm

    # we already imported User in the view code above, remember?
    model = Project

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("main:project_detail",
                       kwargs={"name": self.object.slug})

    def get_object(self):
        # Only get the User record for the user making the request
        return get_objects_for_user(self.request.user, 'main.owns_project').filter(slug=self.kwargs['slug']).first()
