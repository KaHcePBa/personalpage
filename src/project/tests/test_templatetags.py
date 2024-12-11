from unittest import TestCase

from project import templatetags


class Test(TestCase):
    def test_startswith(self):
        check = "xyz"
        dataset = {
            1: False,
            f"2": False,
            f"2{check}": False,
            f"{check}": True,
            f"{check}2": True,
            None: False,
        }

        tag = templatetags.startswith

        for data, expected in dataset.items():
            got = tag(data, check)
            self.assertEqual(
                expected,
                got,
                f"{tag.__name__}({data!r}, {check!r}) -> {got!r} != {expected!r}",
            )

        self.assertIn(tag.__name__, templatetags.register.filters)
