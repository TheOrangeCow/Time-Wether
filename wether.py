import requests
from datetime import datetime, timezone
#openweathermap
def get_weather(postcode):
    api_key = ''
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    params = {
        'zip': f'{postcode},gb',
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data['cod'] == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'], tz=timezone.utc).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data['sys']['sunset'], tz=timezone.utc).strftime('%H:%M:%S')
        rain_chance = data['weather'][0]['main'] == 'Rain'

        print(f"Weather in {postcode}: {weather_description}")
        print(f"Temperature: {temperature}°C (Feels like: {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Sunrise: {sunrise} UTC")
        print(f"Sunset: {sunset} UTC")

        if rain_chance:
            print("It's likely to rain today.")
        else:
            print("No rain expected.")
    else:
        print(f"Postcode {postcode} not found.")
    
postcode = input("Enter UK postcode: ")
get_weather(postcode)
