from django.http import HttpRequest
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

from project.utils import consts
from project.utils.xstatic import get_favicon
from project.utils.xstatic import render_static


@cache_page(consts.AGE_1MONTH)
def view_favicon(request: HttpRequest) -> HttpResponse:
    favicon = get_favicon()
    return render_static(favicon, "image/png")
