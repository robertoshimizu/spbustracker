from pykafka import KafkaClient

if __name__ == '__main__':
    client = KafkaClient(hosts='localhost:9092')
    topic = client.topics['topicname']
    producer = topic.get_sync_producer()
    producer.produce('test message')