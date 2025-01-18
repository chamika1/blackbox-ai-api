from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from .config import VALIDATION_TOKEN

class Message(BaseModel):
    """
    Represents a single message in the chat conversation
    """
    id: str = Field(
        ..., 
        description="Unique identifier for the message",
        example="msg1"
    )
    content: str = Field(
        ..., 
        description="The actual content/text of the message",
        example="Hi, can you help me with Python programming?"
    )
    role: str = Field(
        ..., 
        description="Role of the message sender (user/assistant)",
        example="user"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "msg1",
                    "content": "Hi, can you help me with Python programming?",
                    "role": "user"
                }
            ]
        }
    }

class ChatRequest(BaseModel):
    """
    Request model for chat interactions
    """
    messages: List[Message]
    id: str
    previewToken: Optional[str] = None
    userId: Optional[str] = None
    codeModelMode: bool = True
    agentMode: Dict = {}
    trendingAgentMode: Dict = {}
    isMicMode: bool = False
    userSystemPrompt: Optional[str] = None
    maxTokens: int = 1024
    playgroundTopP: float = 0.9
    playgroundTemperature: float = 0.5
    isChromeExt: bool = False
    githubToken: Optional[str] = None
    clickedAnswer2: bool = False
    clickedAnswer3: bool = False
    clickedForceWebSearch: bool = False
    visitFromDelta: bool = False
    mobileClient: bool = False
    userSelectedModel: str = ""
    validated: str = VALIDATION_TOKEN

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
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
                    "validated": VALIDATION_TOKEN
                }
            ]
        }
    }

class ChatResponse(BaseModel):
    """
    Response model for chat interactions
    """
    message_id: str
    content: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message_id": "550e8400-e29b-41d4-a716-446655440000",
                    "content": "Hello! Yes, I'd be happy to help you with Python programming. What specific topic would you like to learn about?"
                }
            ]
        }
    } 