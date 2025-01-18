import httpx
import json
import asyncio
from time import sleep
import sys

# API endpoint
url = "http://127.0.0.1:8000/chat/1"

# Example conversations
conversations = [
    "Write a Python function to calculate fibonacci numbers",
    "Can you explain how recursion works in programming?",
    "Give me an example of using list comprehension in Python"
]

async def chat_with_ai():
    for message in conversations:
        # Prepare payload
        payload = {
            "messages": [
                {
                    "id": "msg1",
                    "content": message,
                    "role": "user"
                }
            ],
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
            # Send POST request with increased timeout
            timeout = httpx.Timeout(30.0, connect=20.0)
            async with httpx.AsyncClient(timeout=timeout) as client:
                print(f"\nUser: {message}")
                response = await client.post(url, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    print(f"Assistant: {result['content']}")
                else:
                    print(f"Error: Received status code {response.status_code}")
                    print(f"Response: {response.text}")
                
                # Small delay between messages
                await asyncio.sleep(2)  # Using asyncio.sleep instead of time.sleep

        except httpx.TimeoutException:
            print(f"Error: Request timed out for message: {message}")
            continue
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            continue

    try:
        # Get final conversation history
        history_url = "http://127.0.0.1:8000/conversation/1"
        async with httpx.AsyncClient(timeout=timeout) as client:
            history = await client.get(history_url)
            if history.status_code == 200:
                print("\nFull Conversation History:")
                for msg in history.json()['messages']:
                    print(f"\n{msg['role'].title()}: {msg['content']}")
            else:
                print("Error retrieving conversation history")
    except Exception as e:
        print(f"Error retrieving conversation history: {str(e)}")

if __name__ == "__main__":
    try:
        asyncio.run(chat_with_ai())
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1) 