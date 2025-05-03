from flask import Flask, render_template, request
import requests

app = Flask(__name__)# tareeka hai flask ko import karne ka.
# Your weather API key (from a service like OpenWeatherMap)
# city = 'London'
API_KEY = '16a1863427bf48e5c7c5dfc71da6e936'
BASE_URL = f'https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&units=metric'

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Weather info route
@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')

    # Make the API request to OpenWeatherMap
    response = requests.get(BASE_URL,params={'q': city, 'appid': API_KEY, 'units': 'metric'})
    data = response.json()
# print(data)


    if data['cod'] == 200:
        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'icon': data['weather'][0]['icon'],
            'wind_speed': data['wind']['speed'],
            'latitude': data['coord']['lat'],
            'longitude': data['coord']['lon'],
            'country': data['sys']['country'],
            'visibility': data['visibility'],
            'sunrise': data['sys']['sunrise'],
            'sunset': data['sys']['sunset'],
            'timezone': data['timezone'],
        }
        return render_template('index.html', weather=weather)
    else:
        return render_template('index.html', error="City not found!")

if __name__ == '__main__':
    app.run(debug=True)

