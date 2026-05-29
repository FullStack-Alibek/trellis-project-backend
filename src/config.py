from dotenv import load_dotenv
import os

load_dotenv()

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")