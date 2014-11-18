# -*- coding: utf-8 -*-
# Import the reverse lookup function
import json

from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login

# view imports
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

from rest_framework import generics, permissions, status, views
from rest_framework.response import Response

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

# Import the form from users/forms.py
from .forms import UserForm

# Import the customized User model
from .models import User
from .serializers import UserSerializer


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    form_class = UserForm

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                serialized = UserSerializer(user)

                return Response(serialized.data)
            else:
                return Response({
                    'error': 'Awkward! Your account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'error': 'Looks like your username or password is wrong. :('
            }, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({ 'success': True })
