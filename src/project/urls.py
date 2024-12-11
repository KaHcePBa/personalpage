from django.contrib import admin
from django.urls import include, path

from project.views import view_favicon

urlpatterns = [
    # --- admin urls ---
    path('admin/', admin.site.urls),
    # --- static views ---
    path("favicon.png", view_favicon, name="favicon"),
    # --- applications urls ---
    path('', include("applications.index.urls")),
    path('psychedelic/', include("applications.psychedelic.urls")),
    path('projects/', include("applications.projects.urls")),
    path('musicpl/', include("applications.musicpl.urls")),
    path('blog/', include("applications.blog.urls")),
]
