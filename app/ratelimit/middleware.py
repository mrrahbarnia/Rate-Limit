from django.http import HttpResponseForbidden
from django.conf import settings

from .utils import get_client_ip
from .services import get_counter, set_counter, incr_counter

login_rate_limit = int(settings.LOGIN_RATE_LIMIT)
login_sampling_period = int(settings.LOGIN_SAMPLING_PERIOD)

class RateLimiterMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> None:

        client_ip = get_client_ip(request=request)

        if request.path == '/login/':
            counter = get_counter(key=f'count:/login/:{client_ip}')
            if counter:
                if int(counter) >= login_rate_limit:
                    return HttpResponseForbidden('You are blocked from this website.')
                else:
                    incr_counter(key=f'count:/login/:{client_ip}')
            else:
                set_counter(key=f'count:/login/:{client_ip}', ttl=login_sampling_period)

        

        response = self.get_response(request)

        return response

