from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            api_key = '4f2efac6ed38e62570e03ee96c4476a1'
            base_url = 'http://api.openweathermap.org/data/2.5/weather?'
            complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
            response = requests.get(complete_url)
            weather_data = response.json()

    return render_template('index.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
