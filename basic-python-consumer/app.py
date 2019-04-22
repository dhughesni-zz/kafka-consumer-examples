from confluent_kafka import Consumer, KafkaError

print("Start: basic-python-consumer")

props = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'basic-python-consumer3',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(props)

consumer.subscribe(['basic-python-producer-topic'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    print('Received message: {}'.format(msg.value().decode('utf-8')))

consumer.close()

print("End: basic-python-consumer")
