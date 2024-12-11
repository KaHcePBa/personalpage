import random

from django.views.generic import TemplateView
from applications.index.models import IndexInSubInf


class IndexView(TemplateView):
    template_name = "index/index.html"
    model = IndexInSubInf

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        randomized_id = random.randrange(2, 7)  # если нужны от 2 до 8

        try:
            info = IndexInSubInf.objects.get(id=randomized_id)  # если get не находит объекта - ObjectDoesNotExist
        except IndexInSubInf.DoesNotExist:
            info = None # AttributeError: 'NoneType' object has no attribute 'ist'

        if info is None:
            return ctx

        ctx["ist"] = info.ist
        return ctx

