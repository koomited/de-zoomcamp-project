# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Copy only the requirements.txt first to leverage Docker cache
RUN pip install --no-cache-dir -r requirements.txt

# Run coinbase_fetcher.py when the container launches
CMD ["python", "./consumer.py"]
