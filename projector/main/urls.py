from django.conf.urls import url
from main.views import ProjectListView, ProjectDetailView, ProjectUpdateView, ProjectCreateView

urlpatterns = [
    url(r'^projects/$', ProjectListView.as_view(), name='project_list'),
    url(
        r'^projects/create/$',
        view=ProjectCreateView.as_view(),
        name='project_create'
    ),
    url(
        regex=r'^projects/(?P<name>[\w.@+-]+)/$',
        view=ProjectDetailView.as_view(),
        name='project_detail'
    ),
    url(
        regex=r'^projects/(?P<slug>[\w.@+-]+)/update/$',
        view=ProjectUpdateView.as_view(),
        name='project_update'
    ),
]
