from pydantic import BaseModel, Field, StrictStr


class PredictRequest(BaseModel):
    input_text: StrictStr = Field(..., title="input_text", description="Input text", example="Input text for ML")


class PredictResponse(BaseModel):
    result: float = Field(..., title="result", description="Predict value", example=0.9)
