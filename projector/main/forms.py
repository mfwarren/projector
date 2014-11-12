# -*- coding: utf-8 -*-
from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = Project

        # Constrain the UserForm to just these fields.
        fields = ("name",)
