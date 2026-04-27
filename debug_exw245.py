import requests
import os
from dotenv import load_dotenv

load_dotenv()

# SETTINGS
COURSE_ID = "38148"
API_TOKEN = os.getenv('CANVAS_API_TOKEN')
BASE_URL = "https://azwestern.instructure.com"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def force_test_injection():
    url = f"{BASE_URL}/api/v1/courses/{COURSE_ID}/pages/front-page"
    
    # Simple test payload - no complex HTML
    data = {
        "wiki_page": {
            "title": "Debug Test Page",
            "body": "<h1>DEBUG INJECTION</h1><p>Coach Alan - Handshake Test</p>",
            "published": True,
            "front_page": True
        }
    }

    print(f"[*] Attempting injection to {url}...")
    response = requests.put(url, headers=headers, json=data)
    
    print(f"[STATUS CODE]: {response.status_code}")
    print(f"[RESPONSE BODY]: {response.text}")

if __name__ == "__main__":
    force_test_injection()