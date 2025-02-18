from contextlib import closing
from typing import Union

from google_play_scraper.exceptions import NotFoundError, ExtraHTTPError

from urllib.error import HTTPError
from urllib.request import urlopen, Request


def _urlopen(obj):
    data = None
    try:
        with closing(urlopen(obj)) as resp:
            data = resp.read().decode("UTF-8")
    except HTTPError as e:
        if e.code == 404:
            raise NotFoundError("App not found(404).")
        else:
            raise ExtraHTTPError(
                "App not found. Status code {} returned.".format(e.code)
            )
    return data


def post(url: str, data: Union[str, bytes], headers: dict) -> str:
    return _urlopen(Request(url, data=data, headers=headers))


def get(url: str) -> str:
    return _urlopen(url)
