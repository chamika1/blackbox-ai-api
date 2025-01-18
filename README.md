# Blackbox AI Chat API

A FastAPI-based REST API for interacting with Blackbox AI chatbot.

## Features

- Chat with Blackbox AI
- Maintain conversation history
- Token-based authentication
- Docker support
- Cloud deployment ready

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/chamika1/blackbox-ai-api.git
cd blackbox-ai-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the API:
```bash
uvicorn app.main:app --reload
```

4. Visit API documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Using the API Client

```python
from api_client import BlackboxApiClient

# Initialize client
client = BlackboxApiClient()

# Chat with AI
response = client.chat(
    user_id="user123",
    message="How do I write a Python function?"
)
print(f"AI: {response['content']}")

# Get conversation history
history = client.get_conversation("user123")
for msg in history['messages']:
    print(f"{msg['role']}: {msg['content']}")
```

## Docker Support

Run with Docker:
```bash
# Build and run
docker-compose up --build

# Or manually
docker build -t blackbox-api .
docker run -p 8000:80 blackbox-api
```

## Development

1. Install development dependencies:
```bash
pip install pytest pytest-asyncio httpx
```

2. Run tests:
```bash
pytest
```

## Deployment

The API can be deployed to:

### Render
```bash
# Deploy via GitHub integration
1. Connect your GitHub repository
2. Select Docker runtime
3. Deploy
```

### Railway
```bash
# Deploy via CLI
railway up
```

### Environment Variables

- `PORT` - Server port (default: 8000)
- `HOST` - Server host (default: 0.0.0.0)

## API Documentation

### Endpoints

#### POST /chat/{user_id}
Send a message to the AI.

Request:
```json
{
  "messages": [{
    "content": "Hello, how are you?",
    "role": "user"
  }],
  "validated": "your-token-here"
}
```

Response:
```json
{
  "message_id": "uuid",
  "content": "AI response here"
}
```

#### GET /conversation/{user_id}
Get conversation history.

## License

MIT 