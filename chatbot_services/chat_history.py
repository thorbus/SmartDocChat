from datetime import datetime

# In-memory storage for chat history 
chat_history = {}

def store_chat_history(thread_id, sender, message):
    """Store a message in the chat history."""
    if thread_id not in chat_history:
        chat_history[thread_id] = []
    
    chat_history[thread_id].append({
        "sender": sender,
        "message": message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def retrieve_chat_history(thread_id):
    """Retrieve the entire chat history for a given thread_id."""
    return chat_history.get(thread_id, [])
