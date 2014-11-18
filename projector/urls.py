# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from users.views import UserCreateView, LoginView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',


    url(r'^api/v1/users/$', UserCreateView.as_view(), name='user-create'),
    # url(r'^api/v1/users/(?P<pk>[0-9]+)/$',
    #     UserDestroyView.as_view(), name='user-destroy'),
    # url(r'^api/v1/users/(?P<user__username>[a-zA-Z0-9_@+-]+)/$',
    #     UserProfileRetrieveUpdateView.as_view(), name='profile'),
    # url(r'^api/v1/users/(?P<username>[a-zA-Z0-9_@+-]+)/posts/$',
    #     UserPostsListView.as_view(), name='profile-posts'),

    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    # url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    url(r'^.*$',
        TemplateView.as_view(template_name='index.html'), name='index'),

    url(r'^$',  # noqa
        TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

    # Your stuff: custom urls go here
    url(r'', include('main.urls', namespace='main')),

    # REST Framework

    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
