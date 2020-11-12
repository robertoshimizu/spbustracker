from flask import Flask
from flask import stream_with_context
from flask import render_template, Response
import time

from project.usecases.getLinha import SPTrans

app = Flask(__name__)

def stream_api():
    api = SPTrans()
    time.sleep(10)
    api_response = api.getLinha('1189').text
    #print(api_response)
    yield 'data: {}\n\n'.format(api_response)

@app.route('/stream')
@stream_with_context
def stream():
    return Response(stream_api(), mimetype='text/event-stream')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sptrans')
def hello_world():
    api = SPTrans()
    response = api.getLinha('1189')
    # print(response.status_code)
    return str(response.text)


if __name__ == '__main__':
    app.run(debug=True)


