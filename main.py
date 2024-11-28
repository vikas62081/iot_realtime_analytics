
import os
from src.config.kafka_config import KAFKA_TOPIC
from spark.consumer import start_streaming
from src.kafka.producer import produce_messages
from src.utils.sensor_data_simulator import generate_sensor_data
from dotenv import load_dotenv

default_env_file_name=".env"

BASEDIR = os.path.abspath(os.path.dirname(__file__)) 
load_dotenv(os.path.join(BASEDIR, default_env_file_name))

if __name__ == "__main__":
    data=generate_sensor_data()
    produce_messages(topic=KAFKA_TOPIC,data=data)
    start_streaming()
    