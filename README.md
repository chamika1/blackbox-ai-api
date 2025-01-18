# Blackbox AI Chat API

A FastAPI-based REST API for interacting with Blackbox AI chatbot.

## Features

- Chat with Blackbox AI
- Maintain conversation history
- Token-based authentication
- Docker support
- Cloud deployment ready

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/blackbox-ai-api.git
cd blackbox-ai-api

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
uvicorn app.main:app --reload
```

2. Access the API documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

- POST `/chat/{user_id}` - Send a message to the AI
- GET `/conversation/{user_id}` - Get conversation history

## Docker Support

Build and run with Docker:
```bash
# Build the image
docker build -t blackbox-api .

# Run the container
docker run -d -p 80:80 blackbox-api
```

## Deployment

The API can be deployed to:
- Render
- Railway
- Deta Space

## Environment Variables

- `PORT` - Server port (default: 8000)
- `HOST` - Server host (default: 0.0.0.0)

## License

MIT 