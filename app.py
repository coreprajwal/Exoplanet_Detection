from fastapi import FastAPI
from routes import predict
import uvicorn

app=FastAPI()

app.include_router(predict.router,prefix="/predict")

@app.get("/")
def root():
    return { "message": "API is Live", "usage": "Send a POST request to this route with the required JSON body."}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)