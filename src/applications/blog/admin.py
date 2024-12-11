from django import forms
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from applications.blog.models import BlogPost


class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = "__all__"
        widgets = {"ist": forms.Textarea()}


@admin.register(BlogPost)
class BlogAdminModel(ModelAdmin):
    form = BlogAdminForm
