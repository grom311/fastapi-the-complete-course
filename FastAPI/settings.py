from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
DB_PORT=os.getenv('DB_PORT')
print(f"DB_PORT: {DB_PORT}")
print(f"POSTGRES_PASSWORD: {POSTGRES_PASSWORD}")
print(f"POSTGRES_USER: {os.environ.get('POSTGRES_USER')}")