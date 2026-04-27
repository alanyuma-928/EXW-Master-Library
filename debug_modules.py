import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("CANVAS_BASE_URL")
TOKEN = os.getenv("CANVAS_API_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}
CID = os.getenv("ID_EXW245")

res = requests.get(f"{BASE_URL}/courses/{CID}/modules", headers=HEADERS)
print(res.json())
