from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.environ.get("PASSWORD")
EMAIL = os.environ.get("EMAIL")