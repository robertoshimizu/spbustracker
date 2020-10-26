from pykafka import KafkaClient

class Kafka:
    def __init__(self, topicName):
        self.topicName = topicName.encode()
        client = KafkaClient(hosts='localhost:9092')
        self.topic = client.topics[self.topicName]

    def produce(self,message):
        producer = (self.topic).get_producer()
        producer.produce(str(message).encode())
        print(str(message).encode())

    def consume(self):
        consumer = self.topic.get_simple_consumer()
        for message in consumer:
            if message is not None:
                print(message.offset, message.value)

if __name__ == '__main__':
    kafka = Kafka('test_topic')
    for i in range(4):
        message = 'test message {i}'.format(i=i)
        kafka.produce(message)

    kafka.consume()
