from django import forms
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from applications.index.models import IndexInSubInf


class IndexInSubInfAdminForm(forms.ModelForm):
    class Meta:
        model = IndexInSubInf
        fields = "__all__"
        widgets = {"ist": forms.Textarea()}


@admin.register(IndexInSubInf)
class IndexInSubInfAdminModel(ModelAdmin):
    form = IndexInSubInfAdminForm
