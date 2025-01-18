import re
import json
import uuid
from typing import Dict, List
from .models import Message

class ChatService:
    def __init__(self):
        self.user_conversations: Dict[str, List[Message]] = {}

    def clean_response(self, content: str) -> str:
        """
        Clean the response content if it contains unwanted structured data.
        """
        json_start_index = content.find('$~~~$')
        if json_start_index != -1:
            content = content[json_start_index:]
        
        cleaned_content = re.sub(r'\$~~~\$.*?\$~~~\$', '', content).strip()

        if not cleaned_content:
            return "No content available after cleaning."

        try:
            if cleaned_content:
                data = json.loads(cleaned_content)
                if isinstance(data, list):
                    snippets = [item.get('snippet', 'No snippet available') 
                              for item in data if isinstance(item, dict)]
                    return "\n\n".join(snippets)
                return 'No valid snippet found inside the markers.'
            return "No valid JSON content."
        except json.JSONDecodeError:
            return cleaned_content

    def add_message(self, user_id: str, content: str, role: str) -> str:
        """
        Add a message to the conversation history and return the message ID.
        """
        message_id = str(uuid.uuid4())
        if user_id not in self.user_conversations:
            self.user_conversations[user_id] = []
            
        self.user_conversations[user_id].append(
            Message(id=message_id, content=content, role=role)
        )
        return message_id

    def get_conversation(self, user_id: str) -> List[Message]:
        """
        Get the conversation history for a user.
        """
        return self.user_conversations.get(user_id, []) 