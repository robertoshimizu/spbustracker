from flask import Flask
from flask import render_template, Response, stream_with_context
import time
import os

from project.repository.kafka_repository import Kafka
from project.usecases.getLinha import SPTrans

app = Flask(__name__,template_folder='../templates')

def stream_api(kafka):
    i = 0
    api = SPTrans()
    while i < 14:
        i += 1
        time.sleep(2)
        print(kafka.produce(api.getLinha('1189').text))

@app.route('/')
def index():
    kafka = Kafka('busLine')
    #stream_api(kafka)
    #print(os.getcwd())
    print("Iniciando produção de streams da linha de onibus")
    return Response(stream_api(kafka),mimetype = "text/event-stream")
    #return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


