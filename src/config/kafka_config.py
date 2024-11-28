# config/kafka_config.py
# Kafka and ZooKeeper configuration
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"  # Kafka server address
ZOOKEEPER_SERVER = "localhost:2181"         # ZooKeeper server address
KAFKA_TOPIC = "helioport"                   # Kafka topic name

# Kafka consumer settings
CONSUMER_GROUP_ID = "sensor-consumer-group"