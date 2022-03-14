from fastapi import FastAPI, response
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health(response: Response):
    status_code = os.getenv("RETURN_CODE")
    if status_code:
        status_code = int(status_code)
    else:
        status_code = 200
    response.status_code = status_code
    return {"healthcheck_code": status_code}