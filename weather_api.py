import json
import sqlite3
import requests
import numpy as np
import pandas as pd

# OpenWeatherMap API Key
api_key = "ebe4d01c53aef3f296068a0a19528b31"

# Base URL for OpenWeatherMap API
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# City names and coordinates
cities = {
    "Delhi": {"lat": 28.7041, "lon": 77.1025},
    "Mumbai": {"lat": 19.0760, "lon": 72.8777},
    "Chennai": {"lat": 13.0800, "lon": 80.2700},
    "Bangalore": {"lat": 12.9716, "lon": 77.5946},
    "Kolkata": {"lat": 22.5626, "lon": 88.3630},
    "Hyderabad": {"lat": 17.3850, "lon": 78.4867}
}

# Function to convert Kelvin to Celsius and Fahrenheit
def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Connect to SQLite database
conn = sqlite3.connect("weather_data.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        temperature_c REAL,
        feels_like_c REAL,
        temperature_f REAL,
        feels_like_f REAL,
        main TEXT,
        dt INTEGER
    )
""")

# Retrieve and process weather data for each city
for city, coordinates in cities.items():
    params = {
        "lat": coordinates["lat"],
        "lon": coordinates["lon"],
        "appid": api_key,
        "units": "standard"
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    temperature_k = data["main"]["temp"]
    feels_like_k = data["main"]["feels_like"]
    weather_condition = data["weather"][0]["main"]
    timestamp = data["dt"]
    
    temperature_c = kelvin_to_celsius(temperature_k)
    feels_like_c = kelvin_to_celsius(feels_like_k)
    temperature_f = kelvin_to_fahrenheit(temperature_k)
    feels_like_f = kelvin_to_fahrenheit(feels_like_k)
    
    # Insert data into table
    cursor.execute("""
        INSERT INTO weather_data (city, temperature_c, feels_like_c, temperature_f, feels_like_f, main, dt)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (city, temperature_c, feels_like_c, temperature_f, feels_like_f, weather_condition, timestamp))

# Commit changes
conn.commit()

# Roll-up and Aggregate Module
def roll_up_data():
    cursor.execute("SELECT * FROM weather_data")
    data = cursor.fetchall()
    
    # Aggregate data by city and date
    aggregated_data = {}
    for row in data:
        city = row[1]
        date = row[7]
        temperature_c = row[2]
        
        if city not in aggregated_data:
            aggregated_data[city] = {}
        
        if date not in aggregated_data[city]:
            aggregated_data[city][date] = []
        
        aggregated_data[city][date].append(temperature_c)
    
    return aggregated_data

# Alerting Module
def check_alerts(data):
    alerts = []
    
    for city, dates in data.items():
        for date, temperatures in dates.items():
            avg_temperature = np.mean(temperatures)
            
            if avg_temperature > 30:
                alerts.append((city, date, "High Temperature"))
    
    return alerts

# Call roll-up and aggregate module
aggregated_data = roll_up_data()

# Call alerting module
alerts = check_alerts(aggregated_data)

# Print alerts
for alert in alerts:
    print(f"Alert: {alert[0]} on {alert[1]} - {alert[2]}")