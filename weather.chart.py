
import requests
import sqlite3
import matplotlib.pyplot as plt
import schedule
import time 

API_KEY = "ebe4d01c53aef3f296068a0a19528b31"
API_URL = "http://api.openweathermap.org/data/2.5/weather?"

def fetch_weather_data(city):
    params = {"q": city, "units": "metric", "appid": API_KEY}
    response = requests.get(API_URL, params=params)
    
    print(f"API Response Status Code for {city}: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"API Response Data for {city}: {data}")
        return data
    else:
        print(f"Error for {city}: {response.status_code}")
        return None

def create_table(conn, cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        temperature_c REAL,
        feels_like_c REAL,
        main TEXT)
    ''')
    conn.commit()

def insert_data(conn, cursor, city, data):
    print(f"Inserting Data for {city}...")
    
    if data is not None:
        try:
            temp_celsius = data["main"]["temp"]
            feels_like_celsius = data["main"]["feels_like"]
            main_weather = data["weather"][0]["main"]
            
            cursor.execute("INSERT INTO weather_data (city, temperature_c, feels_like_c, main) VALUES (?, ?, ?, ?)",
                           (city, temp_celsius, feels_like_celsius, main_weather))
            conn.commit()
            print(f"Data Inserted Successfully for {city}")
        except KeyError as e:
            print(f"Error Parsing Data for {city}: {e}")
    else:
        print(f"No Data Returned for {city}")

def visualize_data():
    conn = sqlite3.connect("weather_monitoring.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT city, temperature_c FROM weather_data")
    data = cursor.fetchall()
    
    cities = [row[0] for row in data]
    temperatures = [row[1] for row in data]
    
    plt.figure(figsize=(10, 5))
    plt.bar(cities, temperatures)
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")
    plt.title("Weather Data")
    plt.show()

# Database connection
conn = sqlite3.connect("weather_monitoring.db")
cursor = conn.cursor()

# Create table
create_table(conn, cursor)

cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

for city in cities:
    data = fetch_weather_data(city)
    insert_data(conn, cursor, city, data)

# Visualize data
visualize_data()
def fetch_and_visualize_weather():
    # Fetch weather data
    cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
    for city in cities:
        data = fetch_weather_data(city)
        insert_data(conn, cursor, city, data)

    # Visualize weather data
    visualize_data()




