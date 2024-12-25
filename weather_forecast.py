import requests
import json

API_KEY = '4aac4bccfbc748c097f151436242512'  # Replace with your WeatherAPI key
BASE_URL = "http://api.weatherapi.com/v1/current.json?"

def get_weather(city_name):
    complete_url = f"{BASE_URL}key={API_KEY}&q={city_name}"
    response = requests.get(complete_url)
    data = response.json()  # Convert the response to JSON

    # Print the entire response for debugging purposes
    print(json.dumps(data, indent=4))

    if "error" in data:  # Check if there was an error
        print(f"Error: {data['error']['message']}")
        return

    location_data = data.get("location", {})
    current_data = data.get("current", {})

    # Extract relevant data
    city = location_data.get("name", "N/A")
    country = location_data.get("country", "N/A")
    temperature = current_data.get("temp_c", "N/A")
    humidity = current_data.get("humidity", "N/A")
    description = current_data.get("condition", {}).get("text", "N/A")

    # Print weather details
    print(f"City: {city}, {country}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {description}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
