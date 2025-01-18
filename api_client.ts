class BlackboxApiClient {
    private baseUrl: string;

    constructor(baseUrl: string = 'http://127.0.0.1:8000') {
        this.baseUrl = baseUrl;
    }

    async chat(userId: string, message: string) {
        const url = `${this.baseUrl}/chat/${userId}`;
        const payload = {
            messages: [
                {
                    id: 'msg1',
                    content: message,
                    role: 'user'
                }
            ],
            id: 'chat1',
            codeModelMode: true,
            maxTokens: 1024,
            playgroundTopP: 0.9,
            playgroundTemperature: 0.5,
            validated: '00f37b34-a166-4efb-bce5-1312d87f2f94'
        };

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }

    async getConversation(userId: string) {
        const url = `${this.baseUrl}/conversation/${userId}`;
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }
}

// Usage example
async function example() {
    const client = new BlackboxApiClient();

    try {
        // Send a message
        const response = await client.chat(
            'user123',
            'Write a Python function to calculate fibonacci numbers'
        );
        console.log('Assistant:', response.content);

        // Get conversation history
        const history = await client.getConversation('user123');
        console.log('Conversation History:');
        history.messages.forEach(msg => {
            console.log(`${msg.role.charAt(0).toUpperCase() + msg.role.slice(1)}: ${msg.content}`);
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

example(); 