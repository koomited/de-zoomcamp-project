\c postgres;
CREATE TABLE IF NOT EXISTS coinbase (
    time TIMESTAMP NOT NULL,
    price DECIMAL(18,3) NOT NULL,
    type VARCHAR(255) NOT NULL,
    sequence VARCHAR(255) NOT NULL,
    product_id VARCHAR(255) NOT NULL,
    open_24h DECIMAL(18,3) NOT NULL,
    volume_24h DECIMAL(18,3) NOT NULL,
    low_24h DECIMAL(18,3) NOT NULL,
    high_24h DECIMAL(18,3) NOT NULL,
    volume_30d DECIMAL(18,3) NOT NULL,
    best_bid DECIMAL(18,3) NOT NULL,
    best_bid_size DECIMAL(18,3) NOT NULL,
    best_ask DECIMAL(18,3) NOT NULL,
    best_ask_size DECIMAL(18,3) NOT NULL,
    side   VARCHAR(255) NOT NULL,
    trade_id VARCHAR(255) NOT NULL,
    last_size DECIMAL(18,3) NOT NULL
);


