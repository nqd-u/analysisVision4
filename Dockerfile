# Use the official Python image as the base image
FROM python:3.11.5-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Set environment variables for Python (optional)
ENV PYTHONUNBUFFERED=1

# Command to run your Python script
CMD ["python", "caption-image1.py"]
