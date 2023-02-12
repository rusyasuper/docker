# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt /app

COPY notification_manager.py /app

COPY main.py /app

COPY Procfile /app

COPY Arina_baza.db /app

COPY templates /app

COPY static /app

# Install the application dependencies
RUN pip install -r requirements.txt

EXPOSE 80/tcp

RUN gunicorn main:app

## Define the entry point for the container
#CMD ["python", "/app/main.py"]

