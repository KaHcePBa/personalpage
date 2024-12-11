from django.urls import path

from applications.psychedelic.apps import PsychedelicConfig
from applications.psychedelic.views import IndexView

app_name = PsychedelicConfig.label

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
