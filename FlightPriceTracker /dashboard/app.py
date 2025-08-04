import streamlit as st
import pandas as pd
import psycopg2

def load_data():
    conn = psycopg2.connect(dbname="flights_db", user="postgres", password="yourpassword", host="localhost", port="5432")
    df = pd.read_sql("SELECT * FROM flight_prices", conn)
    conn.close()
    return df

st.title("Flight Price Tracker 📈✈️")
df = load_data()
df["route"] = df["source"] + " → " + df["destination"]

route = st.selectbox("Select route", df["route"].unique())
filtered = df[df["route"] == route]
st.line_chart(filtered.set_index("date")["price"])
st.dataframe(filtered)