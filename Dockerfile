# Base image
FROM python:3.11-slim

# Set environment variables
# Do not create unnecessary .pyc files (i.e. __pycache__ folders)
# Print output/logs real-time in Docker containers. Useful for debugging.
ENV PYTHONDONTWRITEBYTECODE=1    
ENV PYTHONUNBUFERED=1     
ENV PYTHONPATH=/app       

# Set working directory
WORKDIR /app

# Install system dependencies
# gcc is a C compiler reuqired to install some dependencies
RUN apt-get update && apt-get install -y gcc    

# Copy dependency files
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install Google Cloud SDK
RUN apt-get update && apt-get install -y curl apt-transport-https gnupg && \
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | \
    tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | \
    apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - && \
    apt-get update && apt-get install -y google-cloud-sdk

# Copy all project files
COPY . .

# Default command
# app(folder).main(main.py):app(FastAPI instance; app=FastAPI())
# --host 0.0.0.0 (Expose the app to all network interfaces. not just localhost)
# uvicorn starts the FastAPI web app servier. It's a fast and lightweight ASGI server used to run FastAPI or other ASGI-based Python web apps.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]                                                                                                                                                            
