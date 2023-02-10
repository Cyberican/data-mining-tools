#!/bin/bash

# Load Resources
apt install python-pdfminer -y
apt install tesseract-ocr-deu -y
apt install ocrmypdf -y
pip install pdfminer --upgrade

# Create buckets
mkdir -vp buckets/{queue,processed,results}

# Install Python packages
pip install -r requirements.txt
