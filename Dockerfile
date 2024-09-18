# Use the Python base image
FROM python:3.12-slim

# Sets the working directory within the container
WORKDIR /app

# Copy the requirements files to the container
COPY requirements.txt requirements.txt

# Installs project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copies the rest of the application files to the container
COPY . .

# Expose the port on which Flask will run
EXPOSE 5000

# Set the command to start the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
