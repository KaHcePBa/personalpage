from django.urls import path

from applications.projects.apps import ProjectsConfig
from applications.projects.views import IndexView

app_name = ProjectsConfig.label

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
