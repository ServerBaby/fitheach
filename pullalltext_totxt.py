# File: pullalltext_totxt.py
# Description: Collects and collates all text from docx and pdf files in a specified folder
# Author: ServerBaby
# Date: 2024-11-05

import os
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

# Main function to process all files in a folder
def extract_text_from_folder(folder_path, output_file_path):
    with open(output_file_path, "w") as output_file:
        for root, _, files in os.walk(folder_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                text = ""
                
                # Process DOCX files
                if filename.endswith(".docx"):
                    text = extract_text_from_docx(file_path)
                # Process PDF files
                elif filename.endswith(".pdf"):
                    text = extract_text_from_pdf(file_path)
                
                # Write extracted text to the output file
                if text:
                    output_file.write(f"--- Text from {filename} ---\n\n")
                    output_file.write(text + "\n\n")
                    output_file.write("====================================\n\n")

# Specify your folder path and output file path
folder_path = r"your_folder_path_here"  # Replace with the path to the folder containing your DOCX and PDF files
output_file_path = "output_filename.txt"  # Replace with the desired name for the output text file

# Run the function
extract_text_from_folder(folder_path, output_file_path)