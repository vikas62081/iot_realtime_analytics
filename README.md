# IOT REALTIME ANALYTICS

1. Create virtual environment just under project folder.

```
    python -m venv .iot-venv
```

2. Execute this command from the root, to activate the virtual environment.

> **Windows**

```
    .iot-venv\Scripts\Activate
```

> **Linux (or) macOS**

```
    source .iot-venv/bin/activate
```

3. Install all the dependencies from requirements.txt

```
    pip install -r server\requirements.txt
```

4. You are almost there!! Just one step away! Just start the server😎

```
    python server\main.py
```

5. start ZooKeeper server

```
bin/zookeeper-server-start.sh config/zookeeper.properties
```

6. start kafka server

```
bin/kafka-server-start.sh config/server.properties
```

7. Create a topic named 'helioport' with 1 partition and 1 replication factor

```

bin/kafka-topics.sh --create --topic helioport --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
