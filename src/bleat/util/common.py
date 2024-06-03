from rich import print
import os

def check_api_key() -> bool:
    if not os.getenv("GOOGLE_API_KEY"):
        return False
    return True
