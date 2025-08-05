from fastapi import APIRouter
from app.schema.predict import PredictResponse,PredictRequest
from app.services.predict_logic import predict_service

router=APIRouter()

@router.post("/",response_model=PredictResponse)
def predict(data:PredictRequest):
       return predict_service(data)