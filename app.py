from flask import Flask, render_template, request
import requests
app = Flask(__name__)
API_KEY = "9d5dd4f024885a5fad65859f34d108a4"  
@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            weather_data = {
                'city': city.title(),
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].title(),
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed']
            }
        else:
            weather_data = {'error': 'City not found'}
    return render_template('index.html', weather=weather_data)
if __name__ == '__main__':
    app.run(debug=True)
