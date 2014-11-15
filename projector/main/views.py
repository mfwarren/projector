from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import ListView
from rest_framework import generics, permissions

from guardian.shortcuts import get_objects_for_user
from guardian.shortcuts import assign_perm

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

from main.models import Project, Task
from .forms import ProjectForm
from .serializers import TaskSerializer


class ProjectListView(ListView):
    model = Project

    def get_queryset(self, *args, **kwargs):
        return get_objects_for_user(self.request.user, ['main.owns_project', 'main.estimate_project', 'main.view_project'], any_perm=True)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
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

    def get_success_url(self):
        return reverse("main:project_detail",
                       kwargs={"name": self.object.slug})


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse("main:project_detail",
                       kwargs={"name": self.object.slug})

    def get_object(self):
        return get_objects_for_user(self.request.user, 'main.owns_project').filter(slug=self.kwargs['slug']).first()


class TaskListCreate(generics.ListCreateAPIView):
    model = Task
    serializer_class = TaskSerializer

    def get_queryset(self, *args, **kwargs):
        return get_objects_for_user(self.request.user, 'main.owns_project').filter(slug=self.kwargs['slug']).first().tasks()

    def get_permissions(self):
        if self.request.method == 'POST':
            return (permissions.IsAuthenticated(),)
        return (permissions.AllowAny(),)

    def pre_save(self, obj):
        obj.author = self.request.user
        return super(TaskListCreate, self).pre_save(obj)


class TaskList(generics.ListAPIView):
    model = Task

    def get_queryset(self, *args, **kwargs):
        return get_objects_for_user(self.request.user, 'main.owns_project').filter(slug=self.kwargs['slug']).first().tasks()


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self, *args, **kwargs):
        return get_objects_for_user(self.request.user, 'main.owns_project').filter(slug=self.kwargs['slug']).first().tasks()

    def get_permissions(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return (IsAuthenticatedAndOwnsObject(),)
        return (permissions.AllowAny(),)
    # def render_to_response(self, context, **response_kwargs):
    #     print context
    #     return self.render_to_json_response(context, **response_kwargs)
