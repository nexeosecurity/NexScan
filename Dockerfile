# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /nexscan

# Copy the requirements file into the container
COPY requirements.txt /nexscan/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /nexscan/

# Set the command to run your Python application
CMD ["python", "NexScan.py"]