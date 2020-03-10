import flask
import random

app = flask.Flask("Theme")
cache = {'id': 0}


@app.route('/colors', methods=['GET'])
def get_time():
    response = {"id": cache['id'],
                "font_color": "#{:06x}".format(random.randint(0, 0xFFFFFF)),
                "background_color": "#{:06x}".format(random.randint(0, 0xFFFFFF))}
    cache['id'] += 1
    return response


if __name__ == '__main__':
    app.run(port=8090)