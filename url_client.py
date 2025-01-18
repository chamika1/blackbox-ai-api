import requests
import uuid
from typing import List, Dict

class ChatSession:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"
        self.conversation_history: List[Dict] = []
        self.session_id = str(uuid.uuid4())

    def chat_with_ai(self, message: str):
        """Send a message and maintain conversation history"""
        url = f"{self.base_url}/chat/msg1"
        
        # Add new message to history
        self.conversation_history.append({
            "id": str(uuid.uuid4()),
            "content": message,
            "role": "user"
        })
        
        payload = {
            "messages": self.conversation_history,  # Send full conversation history
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
            "validated": "00f37b34-a166-4efb-bce5-1312d87f2f94"
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
            
            print(f"\nAI: {result['content']}")
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")
            return None

    def display_history(self):
        """Display the full conversation history"""
        print("\n=== Conversation History ===")
        for msg in self.conversation_history:
            role = "You" if msg["role"] == "user" else "AI"
            print(f"\n{role}: {msg['content']}")
        print("\n==========================")

    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []
        print("\nConversation history cleared.")

def main():
    session = ChatSession()
    print("Chat with AI (type 'exit' to quit, 'history' to see conversation, 'clear' to clear history)")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            break
        elif user_input.lower() == 'history':
            session.display_history()
            continue
        elif user_input.lower() == 'clear':
            session.clear_history()
            continue
        
        session.chat_with_ai(user_input)

if __name__ == "__main__":
    main() 