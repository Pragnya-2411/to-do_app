# Use the official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
