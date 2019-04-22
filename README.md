# kafka-consumer-examples
Basic Apache Kafka Consumer Examples

## References
- https://docs.confluent.io/current/clients/consumer.html
- https://docs.confluent.io/current/clients/confluent-kafka-python/


# *Start Confluent Stack*
```
$ curl -O http://packages.confluent.io/archive/5.2/confluent-5.2.1-2.12.zip
$ unzip confluent-5.2.1-2.12.zip
$ ./confluent-5.2.1/bin/confluent destroy
$ ./confluent-5.2.1/bin/confluent start
```

# BASIC-JAVA-CONSUMER
## Project Setup: basic-java-consumer
```
$ mvn -B archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DgroupId=com.dh.app -DartifactId=basic-java-consumer
```
- https://docs.confluent.io/current/clients/install.html#installation-maven
## To Run: basic-java-consumer
```
kafka-consumer-example/basic-java-consumer $ mvn clean compile exec:java -Dexec.mainClass="com.dh.app.App"
```

---

# BASIC-PYTHON-CONSUMER
## Project Setup: basic-python-consumer
```
kafka-consumer-example $ mkdir basic-python-consumer
<!-- create virtual env -->
kafka-consumer-example/basic-python-consumer $ python3 -m venv venv
<!-- source venv -->
kafka-consumer-example/basic-python-consumer $ source venv/bin/activate
<!-- install confluent_kafka -->
kafka-consumer-example/basic-python-consumer $ pip install confluent_kafka
<!-- export to requirements.txt -->
kafka-consumer-example/basic-python-consumer $ pip freeze > requirements.txt
<!-- make the app file -->
kafka-consumer-example/basic-python-consumer $ touch app.py
```
## To Run: basic-python-consumer
```
kafka-consumer-example/basic-python-consumer $ python3 -m venv venv
kafka-consumer-example/basic-python-consumer $ source venv/bin/activate
kafka-consumer-example/basic-python-consumer $ pip install -r requirements.txt
kafka-consumer-example/basic-python-consumer $ python3 app.py
```