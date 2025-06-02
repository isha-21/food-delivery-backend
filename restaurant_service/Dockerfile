# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install required system dependencies (including PostgreSQL client and networking tools)
RUN apt-get update && \
    apt-get install -y netcat-openbsd gcc libpq-dev postgresql-client && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements file first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make wait-for-db.sh executable
RUN chmod +x wait-for-db.sh

# Use shell form here so env vars expand in ENTRYPOINT
ENTRYPOINT ["./wait-for-db.sh", "db", "postgres", "postgres", "restaurant_db"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
