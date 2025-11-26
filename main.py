import os
from dotenv import load_dotenv
from fastapi import FastAPI
import random
import uvicorn

load_dotenv()

PORT = int(os.getenv("PORT", 8000))
HOST = os.getenv("HOST", "0.0.0.0")


app = FastAPI()

@app.get("/")
def get_random_number():
    return {"wewewe": random.randint(1, 100)}
