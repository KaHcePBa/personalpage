from django.urls import path

from applications.musicpl.apps import MusicPLConfig
from applications.musicpl.views import IndexView

app_name = MusicPLConfig.label

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
