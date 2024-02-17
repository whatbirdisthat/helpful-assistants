import vllm
from fastapi import FastAPI

from clients.VllmClient import VllmClient

app = FastAPI()
llm = VllmClient()

@app.get("/")
async def root():
    return {"message": "Hello World"}
