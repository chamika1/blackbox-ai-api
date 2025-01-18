#!/bin/bash

send_message() {
    local message="$1"
    curl -X 'POST' \
      'http://127.0.0.1:8000/chat/msg1' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d "{
      \"messages\": [
        {
          \"id\": \"msg1\",
          \"content\": \"$message\",
          \"role\": \"user\"
        }
      ],
      \"id\": \"chat1\",
      \"previewToken\": null,
      \"userId\": null,
      \"codeModelMode\": true,
      \"agentMode\": {},
      \"trendingAgentMode\": {},
      \"isMicMode\": false,
      \"userSystemPrompt\": null,
      \"maxTokens\": 1024,
      \"playgroundTopP\": 0.9,
      \"playgroundTemperature\": 0.5,
      \"isChromeExt\": false,
      \"githubToken\": null,
      \"clickedAnswer2\": false,
      \"clickedAnswer3\": false,
      \"clickedForceWebSearch\": false,
      \"visitFromDelta\": false,
      \"mobileClient\": false,
      \"userSelectedModel\": \"\",
      \"validated\": \"00f37b34-a166-4efb-bce5-1312d87f2f94\"
    }"
}

# Example usage
send_message "What is Python?" 