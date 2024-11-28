from kafka import KafkaProducer
import json

from config.kafka_config import KAFKA_BOOTSTRAP_SERVERS

def produce_messages(topic, data):
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    ) 
    for record in data:
        producer.send(topic, record)
    producer.flush()
