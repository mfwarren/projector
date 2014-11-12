from django.conf.urls import url
from main.views import ProjectListView, ProjectDetailView

urlpatterns = [
    url(r'^projects/$', ProjectListView.as_view(), name='project_list'),
    url(
        regex=r'^project/(?P<pk>\d+)/$',
        view=ProjectDetailView.as_view(),
        name='project_detail'
    ),
]
