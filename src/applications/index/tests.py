from django.test import TestCase

from applications.index.views import IndexView
from project.utils.xtests import TemplateResponseTestMixin


class Test(TestCase, TemplateResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/",
            expected_view_name="index:index",
            expected_view=IndexView,
            expected_template="index/index.html",
        )
