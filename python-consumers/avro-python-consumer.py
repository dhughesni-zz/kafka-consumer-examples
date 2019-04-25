from confluent_kafka import KafkaError
from confluent_kafka import Consumer, KafkaError
from confluent_kafka.avro.serializer import SerializerError
from confluent_kafka.avro import CachedSchemaRegistryClient
from confluent_kafka.avro.serializer.message_serializer import MessageSerializer

"""
Due to: Non Java clients (like Go producers, Python, .NET, libserdes) use only the default, TopicNameStrategy 
 - REF: https://docs.confluent.io/current/schema-registry/serializer-formatter.html#limitations
We need to define our own serdes deserializer
"""

print("Start: avro-python-consumer")

props = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'avro-python-consumer_5',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(props)

consumer.subscribe(['avro-python-producer-topic'])

# connect to the schema_registry
schema_registry = CachedSchemaRegistryClient("http://localhost:8081")
# define avro serde - to be used to decode msg value against the avro schema
avro_serde = MessageSerializer(schema_registry)

while True:
    msg = consumer.poll()
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    print('Received message: {}'.format(avro_serde.decode_message(msg.value())))

consumer.close()

print("End: avro-python-consumer")




