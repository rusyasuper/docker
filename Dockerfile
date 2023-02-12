# Use the official Python image as the base image
FROM python:3.9.0

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt

COPY notification_manager.py, main.py, Procfile, Arina_baza.db

COPY templates, static

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["python", "./main.py"]
