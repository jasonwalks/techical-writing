import docx
import re

# Function to extract text from the Word document
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

# Extract text from the Word document
filename = "your_document.docx"
document_text = getText(filename)

# Regex pattern: one or more digits followed by one or more letters (no spaces)
pattern = r'\d+[a-zA-Z]+'

# Use re.findall() to find all occurrences of the pattern in the text
matches = re.findall(pattern, document_text)

# Output the results
print("Found matches:", matches)
