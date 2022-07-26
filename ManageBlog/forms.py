from dataclasses import field
from django import forms
from django.contrib import admin
from froala_editor.widgets import FroalaEditor
from .models import Blog


class BlogForm(forms.ModelForm):

    # content = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Blog
        fields = {'title', 'description', 'content'}
