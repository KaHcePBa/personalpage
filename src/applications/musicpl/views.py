# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
# from django.views import View


# def view_thoughts(request: HttpRequest) -> HttpResponse:
#     return render(request, "musicpl/index.html")
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "musicpl/index.html"
