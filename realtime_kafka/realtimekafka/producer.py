import requests
import json
import time
from kafka import KafkaProducer

class WeatherProducer:
    """ fetches real time weather data and sends it to kafka"""

    def __init__(self,api_key,kafka_topic, kafka_server):
        self.api_key = api_key
        self.kafka_topic = kafka_topic
        self.kafka_server = kafka_server
        self.producer = KafkaProducer(bootstrap_servers=self.kafka_server,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8')
                                      )
        
    def fetch_weather(self):
        """fetches real-time weather data from openweathermap api."""
        url = f"http://api.openweathermap.org/data/2.5/weather?q=Nairobi&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "longitude": data["coord"]["lon"],
                "latitude": data["coord"]["lat"],
                "weather_description": data["weather"][0]["description"],
            }

            self.producer.send(self.kafka_topic, value=weather_data)
            print("sent weather data:", weather_data)

    def start(self,interval=30):
        """continuously fecth and send weather data every interbal seconds"""

        while True:
            self.fetch_weather()
            time.sleep(interval)


if __name__ == "__main__":
    api_key = "8dd6edd262b91b644e5bb2b087e2dc08"
    kafka_topic = "nairobi_weather"
    kafka_server = "localhost:9092"
    producer = WeatherProducer(api_key, kafka_topic, kafka_server)
    producer.start()



