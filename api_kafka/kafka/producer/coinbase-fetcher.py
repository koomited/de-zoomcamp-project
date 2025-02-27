import requests
import time
from kafka import KafkaProducer
from datetime import datetime
import json
import logging
import os
import websocket
import threading
from queue import Queue

# COINBASE
COINBASE_API_URL=os.getenv('COINBASE_API_URL','https://api.coinbase.com/v2/prices/spot?currency=USD')
COINBASE_STATS_URL=os.getenv('COINBASE_STATS_URL')
COINBASE_WS_URL=os.getenv('COINBASE_WS_URL')

# KAFKA
KAFKA_TOPIC=os.getenv('KAFKA_TOPIC','coinbase-topic')
KAFKA_BOOTSTRAP_SERVERS=os.getenv('KAFKA_BOOTSTRAP_SERVERS','kafka:9092')

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                         api_version=(0,11,5),
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))



# Thread-safe queue to store messages
data_queue = Queue()

def on_message(ws, message):
    """Callback for handling incoming WebSocket messages."""
    data = json.loads(message)
    
    # Filter out non-market data (subscription confirmations, heartbeats, etc.)
    if "type" in data and data["type"] == "ticker":
        data_queue.put(data)  # Store only market data in the queue

def on_open(ws):
    """Callback when WebSocket opens, sends subscription message."""
    subscribe_msg = {
        "type": "subscribe",
        "channels": [{"name": "ticker", "product_ids": ["BTC-USD"]}]
    }
    ws.send(json.dumps(subscribe_msg))

def run_websocket():
    """Starts the WebSocket connection in a separate thread."""
    ws = websocket.WebSocketApp(COINBASE_WS_URL, on_message=on_message, on_open=on_open)
    ws.run_forever()

# Start WebSocket in a background thread
ws_thread = threading.Thread(target=run_websocket, daemon=True)
ws_thread.start()

def get_real_time_data():
    """Generator function to yield real-time data."""
    while True:
        data = data_queue.get()  # Retrieve filtered market data from queue
        yield data



def produce_data():
    for data in get_real_time_data():
        if data:
            producer.send(KAFKA_TOPIC, data)
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            logger.info(f"Data sent to Kafka: {data} at : {dt_string}")


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
    logger.info("This is the main")
    produce_data()
