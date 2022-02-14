from typing import Any

from fastapi import APIRouter, Request

from app.models.predict import PredictRequest, PredictResponse

api_router = APIRouter()


@api_router.post("/predict", response_model=PredictResponse)
async def predict(request: Request, payload: PredictRequest) -> Any:
    """
    ML Prediction API
    """
    input_text = payload.input_text
    model = request.app.state.model

    predict_value = model.predict(input_text)
    return PredictResponse(result=predict_value)
