from typing import Optional
import webbrowser

import typer

from urls import shorten_url, store_url, get_url

app = typer.Typer()


@app.command()
def shorten(url: str, code: Optional[str] = typer.Argument(None)):
    try:
        if code is None:
            code = shorten_url(url)
    except ValueError as exc:
        print(exc)
    else:
        stored = store_url(url, code)
        print(code, stored)


@app.command()
def goto(code: str):
    url = get_url(code)
    if url is None:
        print(f"no url found for {code}")
    else:
        webbrowser.open_new(url)


if __name__ == "__main__":
    app()
