from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from applications.blog.models import BlogPost


class AllBlogPostsView(LoginRequiredMixin, ListView):  # LoginRequiredMixin чтобы анонимы не могли оставлять посты
    template_name = "blog/all_posts.html"
    model = BlogPost


class BlogPostsView(LoginRequiredMixin, DetailView):
    template_name = "blog/post.html"
    model = BlogPost
