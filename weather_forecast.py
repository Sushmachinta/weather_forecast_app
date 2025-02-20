import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = '4aac4bccfbc748c097f151436242512'  
BASE_URL = "http://api.weatherapi.com/v1/current.json?"

def get_weather(city_name):
    complete_url = f"{BASE_URL}key={API_KEY}&q={city_name}"
    response = requests.get(complete_url)
    data = response.json()  

    if "error" in data:  
        return None

    location_data = data.get("location", {})
    current_data = data.get("current", {})

  
    city = location_data.get("name", "N/A")
    country = location_data.get("country", "N/A")
    temperature = current_data.get("temp_c", "N/A")
    humidity = current_data.get("humidity", "N/A")
    description = current_data.get("condition", {}).get("text", "N/A")

    return {
        "city": city,
        "country": country,
        "temperature": temperature,
        "humidity": humidity,
        "description": description
    }

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city")
        weather_data = get_weather(city)
        return render_template("index.html", weather_data=weather_data)
    return render_template("index.html", weather_data=None)

if __name__ == "__main__":
    app.run(debug=True)
