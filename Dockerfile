# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY data.py requirements.txt /app/

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run script.py when the container launches
CMD ["python", "data.py"]
