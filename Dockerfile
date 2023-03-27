# Use the official Python image as the parent image
FROM python:3.8-slim-buster

# Set the working directory to /
WORKDIR /

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's source code into the container
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 9999

# Start the MongoDB service and the Flask application
CMD python app.py
