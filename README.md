

## Installation

### 1. Install Dependencies

To install all the necessary dependencies, run the following command:

```bash 
pip install -r requirements.txt
```
### Run the Application

Once the dependencies are installed, you can run the FastAPI application with the following command:

```bash
uvicorn document_preprocessing.main:app --reload
```

By default, this will start the server at http://127.0.0.1:8000
Swagger UI is used by default for API documentation and testing. When you start the FastAPI application, you can access Swagger at http://127.0.0.1:8001/docs.
then  click POST /api/documents/process it will lead to upload file by clicking on try it out button.

## Project Setup
## Document Processing

### Upload and Process Document
To process and store document embeddings in ChromaDB, you need to upload the document using the following endpoint:

- **Endpoint**: `POST /api/documents/process`
- **Input**: File path of the document to be processed.
- **Output** : Asset ID


 ##RAG Chatbot Service
To start the FastAPI application, use `uvicorn` with the following command. This command launches the app in development mode, making it accessible at `http://127.0.0.1:8001/docs`.

```bash
uvicorn chatbot_services.main:app --host 127.0.0.1 --port 8001 --reload

```
1 Chat Backend

The RAG (Retrieval-Augmented Generation) chatbot service is designed to facilitate interactive, document-based responses. It supports multiple chat sessions and ensures that each session references the appropriate document context based on a provided asset ID.

- **Multiple Chats**: The backend can handle multiple chat sessions simultaneously.
- **Asset ID Prompt**: For each new chat, users are prompted to provide an asset ID. This ID links the chat to specific document embeddings stored in ChromaDB.
- **LangChain Agent Integration**: The chat backend integrates with a LangChain-based agent that queries the correct document embeddings using the provided asset ID, allowing for responses directly informed by relevant document content.

#### API Endpoints

- **Start Chat**
    - **Endpoint**: `POST /api/chat/start`
    - **Input**: `asset_id` - the unique ID for the document context.
    - **Output**: A `chat_thread_id` that represents the new chat session.

- **Send Message**
    - **Endpoint**: `POST /api/chat/message`
    - **Input**:
      - `chat_thread_id`: ID of the active chat thread.
      - `user_message`: Message from the user to generate a response.
    - **Output**: The agent's response, streamed for real-time interaction.

### Response Streaming

To improve real-time interaction, response streaming is implemented, allowing the chatbot to deliver responses as they are generated. This helps reduce wait time and enhances the user experience, especially for longer responses.

###  Chat History

For continuity, the service maintains chat histories for each active thread. This feature allows users to view past interactions within the same thread, creating a seamless conversational experience.

#### Chat History API Endpoint

- **Retrieve Chat History**
    - **Endpoint**: `GET /api/chat/history`
    - **Input**: `chat_thread_id` - the ID of the chat thread for which history is being requested.
    - **Output**: Returns the chat history for the specified thread, including all previous messages and responses.

These components together enable a fully functional RAG-based chatbot that supports real-time response streaming and maintains context through stored chat histories.


## Potential Improvements

Here are some suggestions for further improvements or features that could be added to the project:

- **Model Fine-Tuning**: Fine-tune the GPT-2 model on domain-specific data for more accurate and relevant responses.
- **Chat History Management**: Store and retrieve complete chat histories for each session to maintain context across multiple interactions.
- **Multi-threaded Chats**: Support multiple concurrent chat sessions for different users or asset IDs.
- **User Authentication**: Add authentication and user management to allow personalized experiences and history tracking.
- **Better Error Handling**: Implement more robust error handling and validation for requests, including managing database connection errors and edge cases.
- **Performance Optimizations**: Optimize the model's performance for faster response times, possibly by using GPU acceleration or more efficient response generation strategies.






