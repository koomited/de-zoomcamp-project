import streamlit as st
import time
import psycopg2
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Database connection details
DB_HOST = "postgres"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres"
DB_PORT = "5432"

# Function to fetch data from the database
def fetch_data():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT)
        
        cursor = conn.cursor()
        cursor.execute("SELECT time, price FROM coinbase ORDER BY time ASC")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        # Convert to DataFrame
        df = pd.DataFrame(rows, columns=["time", "price"])
        df["time"] = pd.to_datetime(df["time"])  # Ensure time is in datetime format
        return df
    except psycopg2.OperationalError as e:
        st.error(f"Database connection error: {e}")
        return pd.DataFrame(columns=["time", "price"])
    except Exception as e:
        st.error(f"Error: {e}")
        return pd.DataFrame(columns=["time", "price"])

# Main function for Streamlit app
def main():
    st.title("Coinbase Price Time Series")
    st.write("Real-time price updates from PostgreSQL")

    # Create an empty placeholder for the chart
    chart_placeholder = st.empty()

    while True:
        df = fetch_data()
        if not df.empty:
            chart_placeholder.line_chart(df.set_index("time"))  # Plot time series
        else:
            st.write("No data available")

        time.sleep(5)  # Refresh every 5 seconds

if __name__ == "__main__":
    main()
