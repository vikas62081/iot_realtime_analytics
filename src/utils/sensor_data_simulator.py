import re
import random
import string
import datetime
from raw.temp_sensors_data import dic_temp_sensors

# Number of messages to generate
num_msgs = 10  # Change this for the desired number of messages

# Constants for sensor and equipment IDs
id_base_sensor = "S-HAR-PORT-DATA-19951-"
id_base_equipment = "E-HAR-PORT-DATA-25015-"
readout = "iot:reading:sensor:temp"

# Dictionary mappings for sensor data
dic_map_sensor_id = {}
dic_current_temp = {}

# Generates and prints sensor data in JSON format
def generate_sensor_data():
    for _ in range(num_msgs):
        rand_num = str(random.randrange(0, 9)) + str(random.randrange(0, 9)) + str(random.randrange(0, 9))
        rand_letter = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
        rand_temp_value = random.uniform(-5, 5)
        rand_temp_value_delta = random.uniform(-1, 1)

        id_sensor = id_base_sensor + rand_num + rand_letter
        id_equipment = id_base_equipment + rand_num + rand_letter
        sensor = random.choice(list(dic_temp_sensors.keys()))

        if id_sensor not in dic_map_sensor_id:
            dic_map_sensor_id[id_sensor] = sensor
            dic_current_temp[id_sensor] = dic_temp_sensors[sensor] + rand_temp_value
        elif dic_map_sensor_id[id_sensor] != sensor:
            sensor = dic_map_sensor_id[id_sensor]

        temperature = dic_current_temp[id_sensor] + rand_temp_value_delta
        dic_current_temp[id_sensor] = temperature

        today = datetime.datetime.today()
        date_event = today.isoformat()

        json_output = {
            "id_sensor": id_sensor,
            "id_equipment": id_equipment,
            "sensor": sensor,
            "date_event": f"{date_event}Z",
            "standard": {"format": readout},
            "reading": {"temperature": round(temperature, 1)}
        }

        return json_output