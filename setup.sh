#!/bin/bash

# Load Resources
for (( i=0; $i < 1; i++ ))
do
	apt update -y
        apt install python3.10 -y
	apt install python3-pip -y
	apt install python3-pdfminer -y
	apt install tesseract-ocr-deu -y
	apt install ocrmypdf -y
	pip install pdfminer --upgrade
done

# Create buckets
mkdir -vp buckets/{queue,processed,results}

# Install Python packages
pip install -r requirements.txt
