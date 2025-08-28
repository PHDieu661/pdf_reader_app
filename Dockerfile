FROM python:3.11-bullseye

# Install system dependencies
RUN apt-get update && \
    apt-get install -y gcc build-essential && \
    apt-get install -y poppler-utils tesseract-ocr tesseract-ocr-vie libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

# Set Tesseract language data path
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/

# Set work directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Create uploads folder
RUN mkdir -p uploads

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]