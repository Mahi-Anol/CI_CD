# Use an official Python runtime as a parent image
FROM python:3.9-slim


COPY . /app

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 4098 available to the world outside this container
EXPOSE 4098

# Define environment variable

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "4098"]