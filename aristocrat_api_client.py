import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ARISTOCRAT_API_KEY = os.getenv("ARISTOCRAT_API_KEY")
ARISTOCRAT_API_SECRET = os.getenv("ARISTOCRAT_API_SECRET")

def get_ARISTOCRAT():
    headers = {
        "Authorization": f"Bearer {ARISTOCRAT_API_KEY}:{ARISTOCRAT_API_SECRET}",
    }
    response = requests.get("https://api.ARISTOCRAT.fake/v1/ARISTOCRAT", headers=headers)
    return response.json()

if __name__ == "__main__":
    print(get_ARISTOCRAT())
