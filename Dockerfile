# Use a lightweight Python base image
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy our application code
COPY app.py /app

# Install Flask
RUN pip install Flask

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"] 