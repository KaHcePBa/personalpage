from django.http import HttpResponse
from django.test import Client
from django.test import TestCase


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_view_favicon(self):
        resp: HttpResponse = self.cli.get("/favicon.png")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.has_header("Cache-Control"))
        self.assertEqual(resp.get("Cache-Control"), f"max-age={60 * 60 * 24 * 30}")
