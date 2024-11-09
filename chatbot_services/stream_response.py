# stream_response.py
from chatbot_services.response_generator import generate_response


async def stream_response(query, asset_id):
    response = generate_response(query, asset_id)
    for chunk in response:  # Assuming response chunks for streaming
        yield chunk
