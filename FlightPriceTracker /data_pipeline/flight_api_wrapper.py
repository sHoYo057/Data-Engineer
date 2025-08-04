from data_pipeline.scraper import get_flight_data

def fetch_all_routes(city_pairs):
    df_all = []
    for src, dst in city_pairs:
        try:
            df = get_flight_data(src, dst)
            df_all.append(df)
        except Exception as e:
            print(f"Error fetching {src} to {dst}: {e}")
    return pd.concat(df_all, ignore_index=True)