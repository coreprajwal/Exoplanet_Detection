from fastapi import FastAPI
from routes import predict
import uvicorn

app=FastAPI()

app.include_router(predict.router,prefix="/predict")


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)