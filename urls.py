import string
import secrets
from typing import Optional
import zlib

import validators
from hashids import Hashids
import redis

ALPHABET = string.ascii_uppercase + string.digits

rstore = redis.Redis()


def generate_random_shortened_url(n: int = 5) -> str:
    return "".join(secrets.choice(ALPHABET) for _ in range(5))


def shorten_url(url: str) -> str:
    if not validators.url(url):
        raise ValueError(f"{url} is not a valid url")
    crc = zlib.crc32(url.encode("utf-8"))
    hashids = Hashids()
    return hashids.encode(crc)


def store_url(url: str, code: str) -> bool:
    return rstore.set(code, url)


def get_url(code: str) -> Optional[str]:
    url = rstore.get(code)
    return url.decode("utf-8") if url else url


if __name__ == "__main__":
    # generate_random_shortened_url("ajdnaj")
    url = "https://pybit.es/articles/what-we-learned-from-building-our-own-cms-using-django/"
    code = shorten_url(url)
    print(code)
