import fitz  # PyMuPDF
import os
import re
import string  

### This is a script to run through convert your PDFs into Digestible and Cleaned Text Format for the embeddings work 

# Specify the input folder containing the PDF files
input_folder = './PDFs'

# Specify the output folder for the TXT files
output_folder = './genTexts'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def sanitize_text(text):
    """Sanitizes the text by removing unwanted characters and whitespace."""
    # Replace multiple whitespaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Remove non-printable characters
    text = ''.join(filter(lambda x: x in set(string.printable), text))
    return text.strip()

# Iterate over the PDF files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.pdf'):
        # Specify the input PDF file
        input_pdf = os.path.join(input_folder, filename)

        # Specify the output TXT file
        output_txt = os.path.join(output_folder, filename.lower().replace('.pdf', '.txt'))

        # Open the PDF file
        pdf_document = fitz.open(input_pdf)
        
        # Initialize text content
        text_content = []

        # Iterate over the pages in the PDF file
        for page_num in range(len(pdf_document)):
            # Get the page object
            page_object = pdf_document[page_num]

            # Extract the text from the page
            text = page_object.get_text()

            # Sanitize the extracted text
            text = sanitize_text(text)

            # Check if the text is not empty
            if text:
                text_content.append(text)

        # Write the text to the TXT file if content exists
        if text_content:
            with open(output_txt, 'w') as f:
                f.write('\n'.join(text_content))
            print(f'PDF file {filename} converted to TXT successfully!')
        else:
            print(f'Warning: No text extracted from {filename}.')

        # Close the PDF document
        pdf_document.close()
