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
    return {"bebroid228": random.randint(1, 100)}


"""
      # Логін у Docker Hub
      - name: Log in to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      # Build Docker image
      - name: Build Docker image
        run: docker build -t mambodancer/pythonapi:latest .

      # Push Docker image
      - name: Push Docker image
        run: docker push mambodancer/pythonapi:latest

"""