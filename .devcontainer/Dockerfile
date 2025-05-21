# Use your production image as the base
FROM python:3.11-slim

# Install system dependencies needed for development
RUN apt-get update && apt-get install -y \
    gcc \
    git \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1    
ENV PYTHONUNBUFFERED=1     
ENV PYTHONPATH=/app       

WORKDIR /app

# Copy dependency files and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Optionally install dev dependencies (if you have requirements-dev.txt)
# COPY requirements-dev.txt .
# RUN pip install -r requirements-dev.txt

# Copy all project files
COPY . .

# (No CMD here! Codespaces will open a shell by default)
