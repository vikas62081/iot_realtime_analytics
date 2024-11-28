import pyspark
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from pyspark.sql.functions import col, from_json
from src.config.kafka_config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC

temp_data_schema = StructType([StructField("reading", 
                                StructType([StructField("temperature", DoubleType(), True)]), True)])

def start_streaming():
    # Initialize the Spark session
    spark = SparkSession.builder.appName("IoT Real-Time Analytics").getOrCreate()
   
    # Define the schema for the incoming data
    schema = StructType([
        StructField("id_sensor", StringType(), True), 
    StructField("id_equipment", StringType(), True), 
    StructField("sensor", StringType(), True), 
    StructField("date_event", StringType(), True), 
    StructField("standard", temp_data_schema, True)
    ])

    # Read the streaming data from Kafka
    df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
        .option("subscribe", KAFKA_TOPIC) \
        .load()
        
        
     # The Kafka 'value' column is binary, so we need to cast it to string
    df_convert = df.selectExpr("CAST(value AS STRING)")
    query = df_convert.withColumn("jsonData", from_json(col("value"), schema)).select("jsonData.*")
   
    # Block the execution and await termination of the query
    query.awaitTermination()