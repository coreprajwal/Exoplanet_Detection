from fastapi import FastAPI
from app.routes import predict
import uvicorn

app=FastAPI()

app.include_router(predict.router,prefix="/predict")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)