""" Kafka Consumer: A Kafka consumer in my app,
 weather app listens to the nairobi_weather topic and processes real-time weather data sent by the producer. 
 It enables downstream applications to analyze, store, or visualize the weather data as it arrives. """

from kafka import KafkaConsumer
import json

class WeatherConsumer:
    """Consumes real-time weather data from Kafka"""

    def __init__(self, kafka_topic, kafka_server):
        self.consumer = KafkaConsumer(
            kafka_topic,
            bootstrap_servers=kafka_server,  
            auto_offset_reset="latest",
            value_deserializer=lambda x: json.loads(x.decode("utf-8"))
        )

    def get_latest_weather(self):
        """Fetches the latest weather update from Kafka"""
        for message in self.consumer:
            print('received message:', message.value ) # continuosly read the latest weather data
        
if __name__ == "__main__":
    kafka_topic = "nairobi_weather"
    kafka_server = "localhost:9092"
    consumer = WeatherConsumer(kafka_topic, kafka_server)
    print(consumer.get_latest_weather())  # Prints the latest weather data


