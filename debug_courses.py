import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("CANVAS_BASE_URL")
TOKEN = os.getenv("CANVAS_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get(f"{BASE_URL}/courses?per_page=100", headers=HEADERS)
print(response.json())
