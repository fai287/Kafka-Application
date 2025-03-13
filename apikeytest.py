import requests

api_key = '8dd6edd262b91b644e5bb2b087e2dc08'

city = 'Nairobi'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
print(response.json())

