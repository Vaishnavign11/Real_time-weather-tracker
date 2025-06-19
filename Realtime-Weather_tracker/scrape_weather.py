
import requests
from bs4 import BeautifulSoup

def get_weather(city="hyderabad"):
    url = f"https://www.timeanddate.com/weather/india/{city}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        temp_tag = soup.find("div", class_="h2")
        temp = temp_tag.text.strip().replace("°C", "") if temp_tag else None

        if temp:
            return {"city": city, "temperature": float(temp), "description": "N/A"}
        else:
            return {"city": city, "temperature": None, "description": "Temperature not found"}

    except Exception as e:
        print("Scraping error:", e)
        return None

if __name__ == "__main__":
    print(get_weather("hyderabad"))
