import datetime
import flask

app = flask.Flask("Calendar")
cache = {'id': 0}


@app.route('/time', methods=['GET'])
def get_time():
    response = {"id": cache['id'], "time": datetime.datetime.now().strftime("%H:%M:%S")}
    cache['id'] += 1
    return response


@app.route('/date', methods=['GET'])
def get_date():
    response = {"id": cache['id'], "date": datetime.datetime.now().strftime("%d-%m-%Y")}
    cache['id'] += 1
    return response


if __name__ == '__main__':
    app.run(port=8099)
