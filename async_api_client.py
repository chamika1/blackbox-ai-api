import aiohttp
import asyncio

class AsyncBlackboxApiClient:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url

    async def chat(self, user_id: str, message: str) -> dict:
        """Send a chat message and get response"""
        url = f"{self.base_url}/chat/{user_id}"
        
        payload = {
            "messages": [
                {
                    "id": "msg1",
                    "content": message,
                    "role": "user"
                }
            ],
            "id": "chat1",
            "codeModelMode": True,
            "maxTokens": 1024,
            "playgroundTopP": 0.9,
            "playgroundTemperature": 0.5,
            "validated": "00f37b34-a166-4efb-bce5-1312d87f2f94"
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                response.raise_for_status()
                return await response.json()

    async def get_conversation(self, user_id: str) -> dict:
        """Get conversation history"""
        url = f"{self.base_url}/conversation/{user_id}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.json()

async def main():
    client = AsyncBlackboxApiClient()
    
    try:
        # Send a message
        response = await client.chat(
            user_id="user123",
            message="Write a Python function to calculate fibonacci numbers"
        )
        print(f"Assistant: {response['content']}\n")

        # Get conversation history
        history = await client.get_conversation("user123")
        print("Conversation History:")
        for msg in history['messages']:
            print(f"{msg['role'].title()}: {msg['content']}")

    except aiohttp.ClientError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main()) 