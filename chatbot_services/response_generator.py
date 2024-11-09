
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from .chromadb_client import collection  


model_name = "gpt2" 
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def retrieve_docs_from_chromadb(asset_id):
   
    results = collection.query(
        query_texts=[asset_id],  # Query by asset_id or any text
        n_results=1               # Number of relevant documents to retrieve
    )
    
    print(results)
    
    # Assuming results["documents"] is a list of lists or other iterable that may contain non-string elements
    docs = " ".join([str(item) if isinstance(item, str) else " ".join(map(str, item)) for item in results["documents"]])
    
    return docs

def generate_response(user_message: str, asset_id: str):
    # Retrieve relevant document context from ChromaDB
    docs_context = retrieve_docs_from_chromadb(asset_id)
    
    
    combined_input = docs_context + "\nUser: " + user_message

   
    inputs = tokenizer(combined_input, return_tensors="pt", truncation=True).to(device)

    # Generate output with controlled parameters
    outputs = model.generate(
        inputs['input_ids'], 
        max_length=150,  
        num_return_sequences=1, 
        temperature=0.7,
        top_k=50,
        no_repeat_ngram_size=2
    )

    # Decode the output and remove special tokens
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response
