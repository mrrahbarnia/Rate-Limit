from redis import Redis
from django.conf import settings

def connect_redis() -> Redis:
    r = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)
    return r

def get_counter(*, key: str) -> None:
    """count:/login/:{user_ip}"""
    r = connect_redis()
    return r.get(key)

def incr_counter(*, key: str) -> None:
    r = connect_redis()
    r.incr(name=key, amount=1)

def set_counter(*, key: str, value: str = '1', ttl: int) -> None:
    r = connect_redis()
    return r.set(name=key, value=value, ex=ttl)
