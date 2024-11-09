# chat_manager.py
import uuid

class ChatManager:
    def __init__(self):
        self.sessions = {}  # Stores active sessions with their asset IDs and histories

    def start_chat(self, asset_id):
        chat_thread_id = str(uuid.uuid4())
        self.sessions[chat_thread_id] = {
            "asset_id": asset_id,
            "history": []
        }
        return chat_thread_id

    def get_session(self, chat_thread_id):
        return self.sessions.get(chat_thread_id)
