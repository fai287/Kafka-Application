from django.shortcuts import render
from django.http import JsonResponse
from .consumer import WeatherConsumer

kafka_topic = "nairobi_weather"
kafka_server = "localhost:9092"
consumer = WeatherConsumer(kafka_topic, kafka_server)

def get_weather(request):
    """api to return the latest weather data"""
    weather_data = consumer.get_latest_weather()
    return JsonResponse(weather_data)




