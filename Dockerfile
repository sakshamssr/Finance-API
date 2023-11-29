# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Add the Chromium repository and install it
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip

RUN pip install --no-cache-dir pyppeteer
RUN pip install --no-cache-dir pandas
RUN pip install --no-cache-dir beautifulsoup4
RUN pip install --no-cache-dir uvicorn
RUN pip install --no-cache-dir fastapi
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir bs4

# Set the working directory
WORKDIR /app

# Copy all files from the local directory to the container
COPY . /app/

# Set the path to the Chromium executable
ENV PYPPETEER_CHROMIUM_PATH=/usr/bin/google-chrome-stable

# Run your Python script when the container launches
CMD ["python", "server.py"]