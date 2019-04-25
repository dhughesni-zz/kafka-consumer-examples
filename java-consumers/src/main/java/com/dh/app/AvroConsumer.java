package com.dh.app;

import java.time.Duration;
import java.util.Arrays;
import java.util.Properties;

import org.apache.avro.generic.GenericRecord;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;

public class AvroConsumer {

	public static void main(String[] args) {
		
		System.out.println("Start: avro-java-consumer");
		
		Properties props = new Properties();
		props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
		props.put(ConsumerConfig.GROUP_ID_CONFIG, "avro-java-consumer");
		props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");
		props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, "io.confluent.kafka.serializers.KafkaAvroDeserializer");
		props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
		props.put("schema.registry.url", "http://localhost:8081");

		final KafkaConsumer<String, GenericRecord> consumer = new KafkaConsumer<String, GenericRecord>(props);
		String topic = "avro-java-producer-topic";
		consumer.subscribe(Arrays.asList(topic));

		try {
		  while (true) {
		    ConsumerRecords<String, GenericRecord> records = consumer.poll(Duration.ofMillis(100));
		    for (ConsumerRecord<String, GenericRecord> record : records) {
		      System.out.printf("offset = %d, key = %s, value = %s \n", record.offset(), record.key(), record.value());
		    }
		  }
		} finally {
		  consumer.close();
		  System.out.println("End: avro-java-consumer");
		}

	}

}
