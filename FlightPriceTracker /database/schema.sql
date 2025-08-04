CREATE TABLE flight_prices (
    id SERIAL PRIMARY KEY,
    source VARCHAR(50),
    destination VARCHAR(50),
    airline VARCHAR(50),
    price INTEGER,
    date DATE
);