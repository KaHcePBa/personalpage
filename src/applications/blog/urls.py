from django.urls import path

from applications.blog import views
from applications.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path('', views.AllBlogPostsView.as_view(), name="all_posts"),
    path('post/<int:pk>/', views.BlogPostsView.as_view(), name="post"),
]
