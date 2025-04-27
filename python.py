import requests
import json
import datetime

def get_weather(api_key, city):
    """Fetches weather data from OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    except json.JSONDecodeError:
        print("Invalid JSON response received")
        return None

def format_weather_data(weather_data):
    """Formats the weather data for display."""
    if not weather_data:
        return None

    try:
        city = weather_data["name"]
        country = weather_data["sys"]["country"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]
        sunrise_timestamp = weather_data["sys"]["sunrise"]
        sunset_timestamp = weather_data["sys"]["sunset"]

        sunrise_time = datetime.datetime.fromtimestamp(sunrise_timestamp).strftime('%H:%M:%S')
        sunset_time = datetime.datetime.fromtimestamp(sunset_timestamp).strftime('%H:%M:%S')

        formatted_data = f"""
        Weather in {city}, {country}:
        Temperature: {temperature}°C
        Humidity: {humidity}%
        Description: {description}
        Wind Speed: {wind_speed} m/s
        Sunrise: {sunrise_time}
        Sunset: {sunset_time}
        """
        return formatted_data

    except KeyError as e:
        print(f"Missing data in weather response: {e}")
        return None

def main():
    """Main function to get city and API key from user and display weather."""

    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")

    weather_data = get_weather(api_key, city)
    formatted_weather = format_weather_data(weather_data)

    if formatted_weather:
        print(formatted_weather)

if _name_ == "_main_":
    main()