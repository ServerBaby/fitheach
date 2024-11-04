# File: pullalltext_tojson.py
# Description: Collects and collates all text from docx and pdf files in a specified folder 
# and converts that text into json format
# Author: ServerBaby
# Date: 2024-11-05

import os
import json
import pdfplumber
from docx import Document

# Function to extract text from DOCX
def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

# Function to extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# Main function to process all files in a folder and save as JSON
def extract_text_from_folder(folder_path, output_file_path):
    all_data = {}  # Dictionary to store all file content

    for root, _, files in os.walk(folder_path):
        for filename in files:
            # Skip temporary files that start with ~$
            if filename.startswith("~$"):
                continue

            file_path = os.path.join(root, filename)
            text = ""
            
            # Process DOCX files
            if filename.endswith(".docx"):
                text = extract_text_from_docx(file_path)
            # Process PDF files
            elif filename.endswith(".pdf"):
                text = extract_text_from_pdf(file_path)
            
            # Add extracted text to the dictionary with filename as the key
            if text:
                all_data[filename] = text

    # Save all data to a JSON file
    with open(output_file_path, "w", encoding="utf-8") as json_file:
        json.dump(all_data, json_file, indent=4)

# Specify your folder path and output file path
folder_path = r"your_folder_path_here"  # Replace with the path to the folder containing your DOCX and PDF files
output_file_path = "output_filename.json"  # Replace with the desired name for the output json file

# Run the function
extract_text_from_folder(folder_path, output_file_path)
