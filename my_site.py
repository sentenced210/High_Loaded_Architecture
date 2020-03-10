import requests
from flask import Flask, render_template

app = Flask("my_site")


@app.route('/', methods=['GET'])
def response():
    r = requests.request('GET', url="http://localhost:8100/calendar/date")
    date = r.json()["date"]
    r = requests.request('GET', url="http://localhost:8100/calendar/time")
    time = r.json()["time"]
    r = requests.request('GET', url="http://localhost:8100/theme/colors")
    bg_color = r.json()["font_color"]
    txt_color = r.json()["background_color"]
    return render_template("index.html", bg_color=bg_color, txt_color = txt_color, time=time, date=date)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
