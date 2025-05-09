Kafka Data Pipeline Project
===========================
[![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)](#)
[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?logo=visual-studio-code&logoColor=white)](#)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](#)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)](#)
[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](#)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](#)
[![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?logo=apachekafka&logoColor=white)](#)
[![Coinbase](https://img.shields.io/badge/Coinbase-0052FF?logo=coinbase&logoColor=white)](#)
![Awesome](https://img.shields.io/badge/Awesome-ffd700?logo=awesome&logoColor=black)
---

This project sets up a data pipeline to ingest cryptocurrency data from an API, processes it through Kafka and store it in a proper format in postgres. Below you'll find instructions on how I configure the environment to run the services in with docker compose.

Configuration
-------------

Before running the application, you need to set up environment variables that the application will use. Create a `.env` file in the root directory of your project and include the following configurations:

## System Architecture

![System_architecture.png](flow_kafka_stream.drawio.svg)

```bash
# COINBASE
COINBASE_API_URL = https://api.coinbase.com/v2/prices/spot?currency=USD

# KAFKA
KAFKA_TOPIC = coinbase-topic
KAFKA_BOOTSTRAP_SERVERS = kafka:9092
KAFKA_BROKER_ID = 1
KAFKA_ZOOKEEPER_CONNECT = zookeeper:2181
KAFKA_LISTENER_SECURITY_PROTOCOL_MAP = PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
KAFKA_ADVERTISED_LISTENERS = PLAINTEXT://kafka:9092,PLAINTEXT_HOST://localhost:29092
KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR = 1
KAFKA_TRANSACTION_STATE_LOG_MIN_ISR = 1
KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR = 1

# ZOOKEEPER
ZOOKEEPER_CLIENT_PORT = 2181
ZOOKEEPER_TICK_TIME = 2000

# POSTGRES
POSTGRES_USER = postgres
POSTGRES_PASSWORD = postgres
POSTGRES_DB = postgres

```

Please ensure you replace the placeholder values with your actual configurations where necessary.

Running the Application
-----------------------

After setting up the `.env` file, follow the steps below to start your services:

1.  **Build the Docker Images** (if applicable): If you are running your services in Docker containers, make sure to build your images with the Dockerfiles provided in the respective service directories.
    
2.  **Start the Services**: Use Docker Compose or your preferred orchestration tool to start the services defined in your `docker-compose.yml` file. Ensure the `.env` file is correctly referenced in your Docker Compose configuration for environment variables.
    
3.  **Verify Operations**: Once all services are up and running, you can verify their operations by checking logs and ensuring there are no errors during startup and runtime.
    

Additional Information
----------------------

*   **Kafka**: Used for streaming and processing cryptocurrency data in real-time.
*   **Zookeeper**: Required for managing the Kafka cluster.

For further details on configurations and operations, refer to the official documentation of each component.