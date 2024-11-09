import chromadb
from uuid import uuid4
from chatbot_services.chromadb_client import collection

# # Set up the ChromaDB client
# client = chromadb.Client()

# # Get or create a collection in the database
# # collection = client.create_collection("documents")
# collection = get_or_create_collection("documents")

def store_embeddings(embeddings, document_name):
    # Create a unique asset ID for each document
    asset_id = str(uuid4())
    
    # Store the embedding in the database with the associated document name and asset ID
    collection.add(
        documents=[document_name], 
        embeddings=[embeddings],
        metadatas=[{"asset_id": asset_id}],
        ids=[asset_id]
    )
    
  
    return asset_id
