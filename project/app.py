from flask import Flask
from flask import render_template, Response
import time

from project.repository.kafka_repository import Kafka
from project.usecases.getLinha import SPTrans

app = Flask(__name__)

def stream_api(kafka):
    i = 0
    api = SPTrans()

    while i < 4:
        i += 1
        time.sleep(1)
        kafka.produce(api.getLinha('1189').text)


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/sptrans')
def hello_world():
    api = SPTrans()
    response = api.getLinha('1189')
    # print(response.status_code)
    return str(response.text)


if __name__ == '__main__':
    app.run(debug=True)


