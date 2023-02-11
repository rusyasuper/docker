# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /main.py

# Copy the application files into the working directory
COPY . /main.py

ADD https://github.com/rusyasuper/Arrina

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["flask", "run", "--host=0.0.0.0"]
