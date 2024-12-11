from typing import Dict
from typing import Optional

from django.conf import settings
from django.http import HttpRequest

from project.utils import consts


def big_brother(_request: Optional[HttpRequest] = None) -> Dict[str, str]:
    if settings.DEBUG:  # pragma: nocover
        return {}

    return {
        "google_analytics": consts.SCRIPT_GOOGLE_ANALYTICS,
        # "google_tag_manager": consts.SCRIPT_GOOGLE_TAG_MANAGER,
        "yandex_metrika": consts.SCRIPT_YANDEX_METRIKA,
        "yandex_metateg_webmaster": consts.YANDEX_METATEG_WEBMASTER,
        "google_tag_manager_head": consts.SCRIPT_GOOGLE_TAG_MANAGER_HEAD,
        "google_tag_manager_body": consts.SCRIPT_GOOGLE_TAG_MANAGER_BODY,
    }
