
  
import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            description TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_weather(data):
    conn = sqlite3.connect("weather.db")
    c = conn.cursor()
    c.execute("INSERT INTO weather (city, temperature, description, timestamp) VALUES (?, ?, ?, ?)", 
              (data["city"], data["temperature"], data["description"], datetime.now().isoformat()))
    conn.commit()
    conn.close()

  
  
  
# Call once at the start
# init_db()