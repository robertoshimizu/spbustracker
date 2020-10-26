from flask import Flask
from flask import render_template, Response
import time

from project.repository.kafka_repository import Kafka
from project.usecases.getLinha import SPTrans

app = Flask(__name__)

@app.route('/')
def index():
    kafka = Kafka('busLine')
    return Response(kafka.consume(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True,port=5001)


