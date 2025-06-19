
from scrape_weather import get_weather
from db import insert_weather, init_db

init_db()
data = get_weather("hyderabad")
insert_weather(data)
print("Data saved:", data)
