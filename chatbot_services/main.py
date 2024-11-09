
from fastapi import FastAPI, HTTPException
from .chat_manager import ChatManager
from .response_generator import generate_response
from .stream_response import stream_response
from fastapi.responses import StreamingResponse
from .chat_history import store_chat_history, retrieve_chat_history  
app = FastAPI()
chat_manager = ChatManager()

@app.post("/api/chat/start")
async def start_chat(asset_id: str):
    """Start a new chat session."""
    chat_thread_id = chat_manager.start_chat(asset_id)
    return {"chat_thread_id": chat_thread_id}

@app.post("/api/chat/message")
async def send_message(chat_thread_id: str, user_message: str):
    """Send a message in an existing chat thread."""
    session = chat_manager.get_session(chat_thread_id)
    if not session:
        raise HTTPException(status_code=404, detail="Chat thread not found")

    asset_id = session["asset_id"]
    
    # Store the user message in the chat history
    store_chat_history(chat_thread_id, "User", user_message)

    # Generate the bot response based on the user message and asset_id
    response = generate_response(user_message, asset_id)
    
    # Store the bot's response in the chat history
    store_chat_history(chat_thread_id, "Bot", response)

    # Stream the response back to the user
    async def response_streamer():
        async for chunk in stream_response(user_message, asset_id):
            yield chunk

    return StreamingResponse(response_streamer(), media_type="text/plain")

@app.get("/api/chat/{chat_thread_id}/history")
async def get_chat_history(chat_thread_id: str):
    """Retrieve the chat history for a specific chat thread."""
    history = retrieve_chat_history(chat_thread_id)
    if not history:
        raise HTTPException(status_code=404, detail="Chat history not found")
    
    return {"chat_history": history}

