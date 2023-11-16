from flask import Flask, render_template, redirect, url_for
import requests
from datetime import datetime
from awshelper import DBHandler
import time

app = Flask(__name__)
app.config["SECRET_KEY"] = "Password123"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# local consts
API_KEY = "2bedf5814a07c017f5e7f25a251493f4"
LAT, LON = 51.893142, -8.491807

database = DBHandler()


def get_weather_data(city):
    """This function will get the weather data from the API and return it as a dict."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    r = requests.get(url).json()
    r = parser_weather_data(r)
    return r


def parser_weather_data(data):
    """This function will parse the data from the API and return it as a dict."""
    time = datetime.now().strftime("%D | %H:%M:%S")
    city = data["name"]
    weather = data["weather"][0]["main"]
    temperature = data["main"]["temp"]
    wind = data["wind"]["speed"]
    humidity = data["main"]["humidity"]
    return {"time": time, "city": city, "weather": weather, "temperature": temperature, "wind": wind,
            "humidity": humidity}

@app.route("/")
def index():
    data = get_weather_data("Cork")
    table = database.execute("SELECT * FROM weather")
    return render_template("index.html", data=data, table=table)


@app.route("/add")
def add():
    """This function will add an entry to the database."""
    data = get_weather_data("Cork")
    time, city, weather, temperature, wind, humidity = data["time"], data["city"], data["weather"], data["temperature"], data["wind"], data["humidity"]
    database.execute(
        f"INSERT INTO weather (time, city, status, temp, wind, humidity) VALUES ('{time}', '{city}', '{weather}', '{temperature}', '{wind}', '{humidity}')")
    return redirect("/")


