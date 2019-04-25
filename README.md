# kafka-consumer-examples
Basic Apache Kafka Consumer Examples

## References
- https://docs.confluent.io/current/clients/consumer.html
- https://docs.confluent.io/current/clients/confluent-kafka-python/
- https://docs.confluent.io/current/schema-registry/serializer-formatter.html


# *Start Confluent Stack*
```
$ curl -O http://packages.confluent.io/archive/5.2/confluent-5.2.1-2.12.zip
$ unzip confluent-5.2.1-2.12.zip
$ ./confluent-5.2.1/bin/confluent destroy
$ ./confluent-5.2.1/bin/confluent start
```

# JAVA-CONSUMERS
## Project Setup: java-consumers
```
$ mvn -B archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DgroupId=com.dh.app -DartifactId=java-consumers
```
- https://docs.confluent.io/current/clients/install.html#installation-maven
## To Run: java-consumers
```
kafka-consumer-example/java-consumers $ mvn clean compile exec:java -Dexec.mainClass="com.dh.app.BasicConsumer"
kafka-consumer-example/java-consumers $ mvn clean compile exec:java -Dexec.mainClass="com.dh.app.AvroConsumer"
```

---

# PYTHON-CONSUMERS
## Project Setup: python-consumers
```
kafka-consumer-example $ mkdir python-consumers
<!-- create virtual env -->
kafka-consumer-example/python-consumers $ python3 -m venv venv
<!-- source venv -->
kafka-consumer-example/python-consumers $ source venv/bin/activate
<!-- install confluent_kafka -->
kafka-consumer-example/python-consumers $ pip install confluent_kafka
<!-- export to requirements.txt -->
kafka-consumer-example/python-consumers $ pip freeze > requirements.txt
<!-- make the app file -->
kafka-consumer-example/python-consumers $ touch basic-python-consumer.py
kafka-consumer-example/python-consumers $ touch avro-python-consumer.py
```
## To Run: python-consumers
```
kafka-consumer-example/python-consumers $ python3 -m venv venv
kafka-consumer-example/python-consumers $ source venv/bin/activate
kafka-consumer-example/python-consumers $ pip install -r requirements.txt
kafka-consumer-example/python-consumers $ python3 basic-python-consumer.py
kafka-consumer-example/python-consumers $ python3 avro-python-consumer.py
```