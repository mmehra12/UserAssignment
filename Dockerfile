# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables to avoid Python buffering and set the Flask environment
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port on which the Flask app will run
EXPOSE 5000

# Command to run the Flask app with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
