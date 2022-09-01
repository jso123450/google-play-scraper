from typing import Union

from google_play_scraper.exceptions import NotFoundError, ExtraHTTPError

from urllib.error import HTTPError
from urllib.request import urlopen, Request


def _urlopen(obj):
    try:
        with urlopen(obj) as resp:
            return resp.read().decode("UTF-8")
    except HTTPError as e:
        if e.code == 404:
            raise NotFoundError("App not found(404).")
        else:
            raise ExtraHTTPError(
                "App not found. Status code {} returned.".format(e.code)
            )


def post(url: str, data: Union[str, bytes], headers: dict) -> str:
    return _urlopen(Request(url, data=data, headers=headers))


def get(url: str) -> str:
    return _urlopen(url)
