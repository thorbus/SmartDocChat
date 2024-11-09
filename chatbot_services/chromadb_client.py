import os
import chromadb


os.environ["CHROMA_PERSIST_DIRECTORY"] = "chroma_db/"


client = chromadb.Client()

try:
    collection = client.get_collection("documents")
    print("Collection 'documents' already exists.")
except Exception as e:
    print(f"Error: {e}")
    collection = client.create_collection("documents")
    print("Collection 'documents' was created.")

print("Collection setup complete.")
