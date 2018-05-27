import pytz
from django.conf import settings
from django.utils import timezone
from django.utils.translation import LANGUAGE_SESSION_KEY


def user_timezone_middleware(get_response):
    def middleware(request):
        if request.user.is_authenticated:
            tzname = request.user.settings.timezone
            if tzname:
                timezone.activate(pytz.timezone(tzname))
            else:
                timezone.deactivate()

        return get_response(request)

    return middleware


def user_language_middleware(get_response):
    def middleware(request):
        response = get_response(request)

        if request.user.is_authenticated:
            locale = request.user.settings.language

            if hasattr(request, 'session'):
                request.session[LANGUAGE_SESSION_KEY] = locale
            else:
                response.set_cookie(
                    settings.LANGUAGE_COOKIE_NAME, locale,
                    max_age=settings.LANGUAGE_COOKIE_AGE,
                    path=settings.LANGUAGE_COOKIE_PATH,
                    domain=settings.LANGUAGE_COOKIE_DOMAIN,
                )

        return response

    return middleware