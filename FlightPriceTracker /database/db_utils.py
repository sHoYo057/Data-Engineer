import psycopg2

def connect():
    return psycopg2.connect(
        dbname="flights_db",
        user="postgres",
        password="yourpassword",
        host="localhost",
        port="5432"
    )

def insert_flight_data(df):
    conn = connect()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO flight_prices (source, destination, airline, price, date)
            VALUES (%s, %s, %s, %s, %s)
        """, tuple(row))
    conn.commit()
    conn.close()