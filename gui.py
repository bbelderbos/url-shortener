import webbrowser

import PySimpleGUI as sg

from urls import shorten_url, store_url, get_url

sg.theme('DarkAmber')
layout = [
    [
        sg.Text("Enter your URL to shorten: "),
        sg.InputText(key="url")
    ],
    [
        sg.Text("Enter short code (leave empty to use URL): "),
        sg.InputText(key="code"),
    ],
    [
        sg.Button("Shorten"),
    ],
    [
        sg.Text(key="shorten_feedback"),
    ],
    [
        sg.Text("_" * 80),
    ],
    [
        sg.Text("Enter short code to go to page: "),
        sg.InputText(key="goto_code"),
    ],
    [
        sg.Button("Visit"),
    ],
    [
        sg.Text(key="visit_feedback"),
    ],
    [
        sg.Text("_" * 80),
    ],
    [
        sg.Button("Exit"),
    ],
]


window = sg.Window('Window Title', font=("Any 24"), layout=layout)

while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == "Shorten":
        url = values["url"]
        code = values["code"]
        if code == "":
            try:
                code = shorten_url(url)
                window["goto_code"].update(code)
            except ValueError as exc:
                window["shorten_feedback"].update(str(exc))
        stored = store_url(url, code)
        if stored:
            msg = f"Generated short code {code} for url {url}"
        else:
            msg = f"Could not store code {code}"
        window["shorten_feedback"].update(msg)

    if event == "Visit":
        code = values["goto_code"]
        url = get_url(code)
        if url is None:
            msg = f"no URL found for code {code}"
            window["visit_feedback"].update(msg)
        else:
            webbrowser.open_new(url)

window.close()
