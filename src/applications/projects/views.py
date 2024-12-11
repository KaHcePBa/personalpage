# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
# from django.views import View


# def view_projects(request: HttpRequest) -> HttpResponse:
#     return render(request, "projects/index.html")
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "projects/index.html"
