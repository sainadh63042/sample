# Use the official MySQL image from Docker Hub
FROM mysql:latest

# Set the MySQL root password (change to your desired password)
ENV MYSQL_ROOT_PASSWORD=password

# Set the MySQL database and user (change to your desired values)
ENV MYSQL_DATABASE=employees_info
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=Sai@Nadh123

# Expose the MySQL port
EXPOSE 5000

# Install necessary dependencies for the Flask app
#RUN apk update && apk add --no-cache python3 py3-pip

# Set the working directory for the app
WORKDIR /app

# Copy the db_app directory
COPY db_app.py /app

# Copy the database directory
COPY database.py /app

# Copy the config file
COPY config.json /app

# Install Flask and MySQL client for Python
RUN pip3 install Flask mysql-connector-python

# Run the MySQL server and Flask app on container startup
CMD ["sh", "-c", "service mysql start && python3 db_app.py"]

# Note: You'll need to have the Flask app code in a directory named 'app' next to this Dockerfile. 

