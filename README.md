## SPTrans API Stream to Kafka

The goal of this project is to experiment with SPTrans API, stream data to kafka and deploy a client to consume it and render the information in a web page.

#### Kafka

1. Download and start Confluent plataform using docker.
- Clone the [confluentinv/cp-all-in-one](https://github.com/confluentinc/cp-all-in-one) github repository;
- Navigate to the `cp-all-in-one-community` directory;
- Start Confluent Platform specifying the '-d' option to run in detached mode:
```Shell
docker-compose up -d
```
- Verify that the services are up and running:
```Shell
docker-compose ps
```

#### Pykafka Library
Install pykafka library. Below there are two resources:
- pykafka [official documentation]()
- article ["PyKafka: Fast, Pythonic Kafka, at Last!"](https://blog.parse.ly/post/3886/pykafka-now/)
- article ["3 Libraries You Should Know to Master Apache Kafka in Python"](https://towardsdatascience.com/3-libraries-you-should-know-to-master-apache-kafka-in-python-c95fdf8700f2)

Start a python console and give it a try. Make sure the docker containers are running.

Also, you can run in isolation the `./project/repository/kafka_repository.py` and observe the output in the terminal.