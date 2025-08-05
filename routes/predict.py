## Adding Routes
from fastapi import APIRouter
from schema.predict import PredictResponse,PredictRequest
from services.predict_logic import predict_service

router=APIRouter()

@router.post("/",response_model=PredictResponse)
def predict(data:PredictRequest):
       return predict_service(data)