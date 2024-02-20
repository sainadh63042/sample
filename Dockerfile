# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /xmljson_con

# Copy the current directory contents into the container at /app
COPY xmltojson.py /xmljson_con

RUN pip install xmltodict

# Run the Python script when the container launches
ENTRYPOINT ["python", "xmltojson.py"]

