from fastapi import FastAPI, UploadFile, File
from .embeddings import create_embeddings
from .file_reader import read_file
from .storage import store_embeddings

app = FastAPI()

@app.post("/api/documents/process")
async def process_document(file: UploadFile = File(...)):
    # Read the content of the uploaded file
    content = await read_file(file)

    # Create embeddings from the file content
    embeddings = create_embeddings(content)

    # Store the embeddings in a vector database and get an asset ID
    asset_id = store_embeddings(embeddings, file.filename)

    # Return the asset ID as a response
    return {"asset_id": asset_id}
