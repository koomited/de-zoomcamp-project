from kafka import KafkaConsumer
import psycopg2
import json
import logging
import os



## Connect to Postgres
def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            user=os.getenv('POSTGRES_USER','postgres'),
            password=os.getenv('POSTGRES_PASSWORD','postgres'),
            host=os.getenv('POSTGRES_HOST','postgres'),
            port=os.getenv('POSTGRES_PORT','5432'),
            dbname=os.getenv('POSTGRES_DB','postgres')
        )
        return connection
    except Exception as e:
        logging.error(f"Error: {e}")
        return connection
    
conn = create_connection()

cursor = conn.cursor()

# KAFKA
KAFKA_TOPIC=os.getenv('KAFKA_TOPIC','coinbase-topic')
KAFKA_BOOTSTRAP_SERVERS=os.getenv('KAFKA_BOOTSTRAP_SERVERS','kafka:9092')


consumer = KafkaConsumer(KAFKA_TOPIC,
                        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))


for message in consumer:
    data = message.value
#" Insert data into Postgres
    cursor.execute("""
            INSERT INTO coinbase (time, price, type, sequence, product_id, open_24h, volume_24h, low_24h,
                                high_24h, volume_30d, best_bid, best_bid_size, best_ask, best_ask_size, 
                                side, trade_id, last_size)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            data['time'], data['price'], data['type'], data['sequence'], data['product_id'], 
            data['open_24h'], data['volume_24h'], data['low_24h'], data['high_24h'], 
            data['volume_30d'], data['best_bid'], data['best_bid_size'], data['best_ask'], 
            data['best_ask_size'], data['side'], data['trade_id'], data['last_size']
        ))

    conn.commit()
    logging.info(f"Data inserted: {data}")
    
    
# cursor.close()
