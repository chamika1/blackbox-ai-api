from typing import Dict

# API Configuration
VALIDATION_TOKEN = "00f37b34-a166-4efb-bce5-1312d87f2f94"

# Headers and Cookies for BlackBox AI
HEADERS: Dict[str, str] = {
    'accept': '*/*',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.blackbox.ai',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

COOKIES: Dict[str, str] = {
    'sessionId': '60da9ffd-8a45-475a-bff2-3745892f516c',
    'intercom-id-jlmqxicb': 'd4a9dec8-fbfb-4b1c-8c85-80d83589ae28',
    'intercom-device-id-jlmqxicb': 'dfcc2489-2b31-49ae-b90d-672f0c5e222f',
    'g_state': '{"i_l":0}',
    '__Host-authjs.csrf-token': '5caba2b81667a94883738b9ed26a4e80198a9795acf78cec982169736887826c%7C5489183c905075535234f0924158f62310d213ed314c28b5c13a7fa74292b912',
    'intercom-session-jlmqxicb': 'VXQyTGNsUW9namFTaUJid2E5OHRoZ3BkUEVuODNJNWYxS3VKSG1zZ2dBWkRLZlhCUVJoS0xpbE9uS0h2M3poRC0tcE4reDhaM1FXRllWSU8xNmEvNVpxQT09--e929cf570cf0c0fe3fafe009ea98981e3ded67c5',
    '__Secure-authjs.callback-url': 'https%3A%2F%2Fwww.blackbox.ai%2F'
} 