from flask import Flask
from flask import render_template, Response
import time


from project.usecases.apiController import ApiController
from project.usecases.getLinha import SPTrans

app = Flask(__name__)

def stream_api():
    i = 0
    api = SPTrans()
    while i < 20:
        i += 1
        time.sleep(5)
        yield api.getLinha('1189').text


@app.route('/')
def index():

    return Response(stream_api(), mimetype='text/event-stream')

@app.route('/sptrans')
def hello_world():
    api = SPTrans()
    response = api.getLinha('1189')
    # print(response.status_code)
    return str(response.text)


if __name__ == '__main__':
    app.run(debug=True)


