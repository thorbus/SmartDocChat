from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(text: str):
    # Convert text into embeddings using the SentenceTransformer model
    
    return model.encode(text)
