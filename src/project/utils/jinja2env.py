import jinja2
from django.conf import settings
from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment

from project.utils import consts
from project.utils.xtemplates import big_brother


def build_jinja2_environment(**options) -> Environment:
    undefined_cls = (jinja2.ChainableUndefined, jinja2.DebugUndefined)[settings.DEBUG]

    opts = options.copy()
    opts.update(
        {"auto_reload": True, "undefined": undefined_cls, }
    )

    env = Environment(**opts)

    global_names = {
        "debug": settings.DEBUG,
        "project_name": consts.PROJECT_NAME.lower(),
        "repr": repr,
        "static": static,
        "url": reverse,
    }

    global_names.update(big_brother())

    env.globals.update(**global_names)

    return env
