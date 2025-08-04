import requests
import pandas as pd
from datetime import date, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def get_flight_data(from_city='DEL', to_city='BOM'):
    url = "https://skyscanner44.p.rapidapi.com/search"
    departure = (date.today() + timedelta(days=3)).strftime("%Y-%m-%d")

    querystring = {
        "adults": "1",
        "origin": from_city,
        "destination": to_city,
        "departureDate": departure,
        "currency": "INR"
    }

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "skyscanner44.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    flights = []
    for flight in data.get("itineraries", []):
        leg = flight["legs"][0]
        flights.append({
            "source": from_city,
            "destination": to_city,
            "airline": leg.get("carriers", [{}])[0].get("name", "Unknown"),
            "price": flight.get("pricingOptions", [{}])[0].get("price", {}).get("amount", 0),
            "date": leg.get("departureDateTime", "").split("T")[0]
        })

    return pd.DataFrame(flights)