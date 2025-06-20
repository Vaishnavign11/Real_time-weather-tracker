# Real_time-weather-tracker

![Screenshot 2025-06-19 160204](https://github.com/user-attachments/assets/3f386150-0241-4dc7-af5d-49d162cb63e4)


# 📦 Features
🌐 Scrapes real-time temperature data from the web

🗃️ Stores weather data in an SQLite database (weather.db)

📈 Visualizes temperature trends with timestamps

🧪 Simple and customizable architecture

🧑‍💻 Built using Python, Streamlit, BeautifulSoup, and Pandas



# 📌 Requirements
Python 3.7+

Libraries:

requests

beautifulsoup4

pandas

matplotlib

streamlit

sqlite3 (built into Python)


# steps:
    📌  Install Required Packages
        pip install requests beautifulsoup4 pandas matplotlib streamlit

    📌  Project Structure
    
        weather-tracker/
      ├── app.py                # Streamlit dashboard
      ├── db.py                 # Database creation & insertion
      ├── run.py                # Run this to scrape & save weather
      ├── scrape_weather.py     # Scraper logic using BeautifulSoup
      ├── weather.db            # SQLite DB (created after running)
      ├── venv/                 # Virtual environment (optional)

    📌 a. Scrape and Insert Weather Data
            python run.py

        b.Launch the dashboard
            streamlit run app.py


🚀 Future Ideas
Add more cities

Schedule automatic updates

Export weather data to CSV/Excel

Use a stable free weather API


