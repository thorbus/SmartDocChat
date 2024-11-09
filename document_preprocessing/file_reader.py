from io import BytesIO
from PyPDF2 import PdfReader
from fastapi import UploadFile

# Function to read the file and process the PDF content
async def read_file(file: UploadFile):
    # Read the file content into bytes
    file_content = await file.read()
    return read_pdf(file_content)

# Function to process a PDF file from bytes
def read_pdf(file_content: bytes):
    # Convert bytes to a file-like object
    file_like_object = BytesIO(file_content)
    
    # Create PdfReader with the file-like object
    reader = PdfReader(file_like_object)
    
    # Extract text from the PDF
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    return text
