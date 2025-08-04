from data_pipeline.flight_api_wrapper import fetch_all_routes
from database.db_utils import insert_flight_data

def run_etl():
    city_pairs = [("DEL", "BOM"), ("BLR", "DEL"), ("HYD", "MAA")]
    df = fetch_all_routes(city_pairs)
    insert_flight_data(df)

if __name__ == "__main__":
    run_etl()