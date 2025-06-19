
import streamlit as st 
import pandas as pd 
import sqlite3

def load_data():
  conn =sqlite3.connect("weather.db")
  df=pd.read_sql_query("select * from weather order by timestamp desc limit 20",conn)
  conn.close()
  df["timestamp"] = pd.to_datetime(df["timestamp"])
  return df

st.title("🌤️ Real-Time Weather Tracker")


df = load_data()
st.line_chart(df.set_index("timestamp")["temperature"])
st.dataframe(df)
