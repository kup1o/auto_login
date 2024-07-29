# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV DISPLAY=:99

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    xvfb \
    unzip \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcairo2 \
    libcups2 \
    libcurl4 \
    libdbus-1-3 \
    libgbm1 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libu2f-udev \
    libvulkan1 \
    libxcomposite1 \
    libxdamage1 \
    libxkbcommon0 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome (version 126.0.6478.182)
RUN wget https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_126.0.6478.182-1_amd64.deb \
    && dpkg -i google-chrome-stable_126.0.6478.182-1_amd64.deb || apt-get install -f -y \
    && apt-mark hold google-chrome-stable \
    && rm google-chrome-stable_126.0.6478.182-1_amd64.deb

# Install ChromeDriver (version 126.0.6478.182)
RUN wget https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.182/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip \
    && mv chromedriver-linux64/chromedriver /usr/bin/chromedriver \
    && rm -r chromedriver-linux64 chromedriver-linux64.zip

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run xvfb in the background
RUN Xvfb :99 -screen 0 1280x800x24 &

# Run the application
CMD ["bash", "-c", "sleep 2; python /app/main.py"]
