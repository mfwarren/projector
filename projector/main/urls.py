from django.conf.urls import url
from main.views import ProjectListView, ProjectDetailView, ProjectUpdateView, ProjectCreateView

urlpatterns = [
    url(r'^projects/$', ProjectListView.as_view(), name='project_list'),
    url(
        regex=r'^project/(?P<pk>\d+)/$',
        view=ProjectDetailView.as_view(),
        name='project_detail'
    ),
    url(
        regex=r'^project/update/$',
        view=ProjectUpdateView.as_view(),
        name='project_update'
    ),
    url(
        regex=r'^project/new/$',
        view=ProjectCreateView.as_view(),
        name='project_new'
    ),
]
