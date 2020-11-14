from flask import Flask
from flask import stream_with_context
from flask import render_template, Response
import time

from project.usecases.getLinha import SPTrans

app = Flask(__name__)

def stream_oneLine():
    api = SPTrans()
    time.sleep(10)
    api_response = api.getLinha('32769').text
    #print(api_response)
    yield 'data: {}\n\n'.format(api_response)

def stream_allLines():
    api = SPTrans()
    time.sleep(10)
    api_response = api.getAllLinhas().text
    #print(api_response)
    yield 'data: {}\n\n'.format(api_response)

@app.route('/oneline')
@stream_with_context
def stream():
    return Response(stream_oneLine(), mimetype='text/event-stream')

@app.route('/alllines')
@stream_with_context
def streamAll():
    return Response(stream_allLines(), mimetype='text/event-stream')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sptrans')
def embed():
    return render_template('frame.html')

@app.route('/livetracker')
def show():
    return render_template('livetracker.html')


if __name__ == '__main__':
    app.run(debug=True)


