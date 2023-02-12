# Use the official Python image as the base image
FROM python:3.9.0

# Set the working directory in the container
WORKDIR /Экслюзив

COPY requirements.txt requirements.txt

COPY notification_manager.py notification_manager.py

COPY main.py main.py

COPY Procfile Procfile

COPY Arina_baza.db Arina_baza.db

COPY templates templates

COPY static static

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["python", "./main.py"]
