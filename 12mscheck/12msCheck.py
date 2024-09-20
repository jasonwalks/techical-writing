import os
import docx
import re

# Function to extract text from a Word document
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

# Function to process all .docx files in the specified directory
def process_docx_files(directory):
    # Regex pattern: one or more digits followed by one or more letters (no spaces)
    pattern = r'\d+[a-zA-Z]+'

    # Loop through all files in the directory
    for file_name in os.listdir(directory):
        # Only process .docx files
        if file_name.endswith('.docx'):
            file_path = os.path.join(directory, file_name)

            # Extract text from the current Word file
            document_text = getText(file_path)

            # Use re.findall() to find all occurrences of the pattern in the text
            matches = re.findall(pattern, document_text)

            # Output the results for this file
            print(f"File: {file_name}")
            if matches:
                print("  Found matches:", matches)
            else:
                print("  No matches found.")
            print()

# Specify the directory containing the .docx files under Downloads/12mscheck
directory = os.path.expanduser("~/Downloads/12mscheck")

# Process all .docx files in the directory
process_docx_files(directory)
