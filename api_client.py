import requests
import json
import uuid
from typing import List, Dict
from app.config import VALIDATION_TOKEN

class BlackboxApiClient:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url
        self.conversation_history: List[Dict] = []

    def chat(self, user_id: str, message: str) -> dict:
        """Send a chat message and get response"""
        url = f"{self.base_url}/chat/{user_id}"
        
        # Add user message to history
        self.conversation_history.append({
            "id": str(uuid.uuid4()),
            "content": message,
            "role": "user"
        })
        
        payload = {
            "messages": self.conversation_history,
            "id": "chat1",
            "previewToken": None,
            "userId": None,
            "codeModelMode": True,
            "agentMode": {},
            "trendingAgentMode": {},
            "isMicMode": False,
            "userSystemPrompt": None,
            "maxTokens": 1024,
            "playgroundTopP": 0.9,
            "playgroundTemperature": 0.5,
            "isChromeExt": False,
            "githubToken": None,
            "clickedAnswer2": False,
            "clickedAnswer3": False,
            "clickedForceWebSearch": False,
            "visitFromDelta": False,
            "mobileClient": False,
            "userSelectedModel": "",
            "validated": VALIDATION_TOKEN
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            result = response.json()
            
            # Add AI response to history
            self.conversation_history.append({
                "id": result["message_id"],
                "content": result["content"],
                "role": "assistant"
            })
            
            return result
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {str(e)}")
            raise

    def get_conversation(self, user_id: str) -> dict:
        """Get conversation history"""
        url = f"{self.base_url}/conversation/{user_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting conversation: {str(e)}")
            raise

    def display_history(self):
        """Display the current conversation history"""
        print("\n=== Conversation History ===")
        for msg in self.conversation_history:
            role = "You" if msg["role"] == "user" else "AI"
            print(f"\n{role}: {msg['content']}")
        print("\n==========================")

    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []
        print("\nConversation history cleared.")

def interactive_chat():
    """Run an interactive chat session"""
    client = BlackboxApiClient()
    user_id = "user123"
    
    print("Chat with AI (type 'exit' to quit, 'history' to see conversation, 'clear' to clear history)")
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                break
            elif user_input.lower() == 'history':
                client.display_history()
                continue
            elif user_input.lower() == 'clear':
                client.clear_history()
                continue
            
            # Send message and get response
            response = client.chat(user_id, user_input)
            print(f"\nAI: {response['content']}")
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            continue

if __name__ == "__main__":
    interactive_chat() 