import os
from fastapi import FastAPI, HTTPException, Path, Body
from .models import ChatRequest, ChatResponse, Message
from .services import ChatService
from .config import HEADERS, COOKIES, VALIDATION_TOKEN
import httpx
import uuid
from typing import Dict, List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Blackbox AI Chat API",
    description="""
    An API for interacting with the Blackbox AI chatbot.
    This API allows you to send messages and maintain conversation history.
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Get port from environment variable
PORT = int(os.getenv("PORT", 8000))
HOST = os.getenv("HOST", "0.0.0.0")

# Update CORS settings for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-frontend-domain.com",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chat_service = ChatService()

async def call_blackbox_ai(request: ChatRequest):
    """Make actual API call to BlackBox AI"""
    url = "https://www.blackbox.ai/api/chat"
    
    timeout = httpx.Timeout(30.0, connect=20.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            response = await client.post(
                url,
                json=request.dict(),
                headers=HEADERS,
                cookies=COOKIES
            )
            
            if response.status_code == 200:
                return response.text
            else:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Error from BlackBox AI API: {response.text}"
                )
        except httpx.TimeoutException:
            raise HTTPException(
                status_code=504,
                detail="Request to BlackBox AI timed out"
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error communicating with BlackBox AI: {str(e)}"
            )

@app.post(
    "/chat/{user_id}",
    response_model=ChatResponse,
    tags=["chat"],
    summary="Send a message to the AI",
    responses={
        200: {
            "description": "Successful response from AI",
            "content": {
                "application/json": {
                    "example": {
                        "message_id": "550e8400-e29b-41d4-a716-446655440000",
                        "content": "Hello! Yes, I'd be happy to help you with Python programming."
                    }
                }
            }
        },
        400: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "No messages provided"
                    }
                }
            }
        },
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid validation token"
                    }
                }
            }
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Error communicating with BlackBox AI"
                    }
                }
            }
        }
    },
    description="""
    Send a message to the AI and get a response.
    
    Authentication:
    - Requires a valid validation token (configured in config.py)
    - Token must be provided in the request body
    
    Parameters:
    - user_id: Unique identifier for the user
    - request: Chat request containing the message and configuration
    
    Returns:
    - ChatResponse containing the AI's response
    
    Example:
    ```python
    from app.config import VALIDATION_TOKEN
    
    client = BlackboxApiClient()
    response = client.chat(
        user_id="user123",
        message="How do I write a Python function?"
    )
    print(response['content'])
    ```
    
    Error Responses:
    - 400: Missing messages in request
    - 401: Invalid or missing validation token
    - 500: Internal server error or AI service error
    """
)
async def chat(
    user_id: str = Path(..., description="Unique identifier for the user"),
    request: ChatRequest = Body(
        ..., 
        description="Chat request containing message and configuration",
        example={
            "messages": [{
                "id": "msg1",
                "content": "Hi, can you help me with Python programming?",
                "role": "user"
            }],
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
            "validated": VALIDATION_TOKEN  # Use actual token from config
        }
    )
):
    try:
        # Validate the request
        if not request.messages:
            raise HTTPException(status_code=400, detail="No messages provided")
        
        if not request.validated or request.validated != VALIDATION_TOKEN:
            raise HTTPException(status_code=401, detail="Invalid validation token")

        # Add user message to conversation
        message_id = chat_service.add_message(
            user_id=user_id,
            content=request.messages[-1].content,
            role="user"
        )

        try:
            # Make actual API call to BlackBox AI
            response_content = await call_blackbox_ai(request)
            cleaned_response = chat_service.clean_response(response_content)

            # Add assistant response to conversation
            chat_service.add_message(
                user_id=user_id,
                content=cleaned_response,
                role="assistant"
            )

            return ChatResponse(
                message_id=message_id,
                content=cleaned_response
            )
        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error processing request: {str(e)}"
            )

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )

@app.get(
    "/conversation/{user_id}",
    response_model=Dict[str, List[Message]],
    tags=["chat"],
    summary="Get conversation history",
    description="""
    Retrieve the conversation history for a specific user.
    
    Parameters:
    - user_id: Unique identifier for the user
    
    Returns:
    - Dictionary containing the list of messages in the conversation
    
    Example:
    ```python
    client = BlackboxApiClient()
    history = client.get_conversation("user123")
    for msg in history['messages']:
        print(f"{msg['role']}: {msg['content']}")
    ```
    """
)
async def get_conversation(
    user_id: str = Path(..., description="Unique identifier for the user")
):
    return {"messages": chat_service.get_conversation(user_id)} 