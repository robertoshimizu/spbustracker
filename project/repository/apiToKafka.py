from project.repository.kafka_repository import Kafka
from project.usecases.getLinha import SPTrans
import time


def stream_api(kafka):
    i = 0
    api = SPTrans()

    while i < 4:
        i += 1
        time.sleep(1)
        #print(api.getLinha('1189').text)
        kafka.produce(api.getLinha('1189').text)

class InteAPIKafka():
    def test_something(self):
        kafka = Kafka('Line1189')
        stream_api(kafka)
        kafka.consume()


if __name__ == '__main__':
    InteAPIKafka().test_something()
