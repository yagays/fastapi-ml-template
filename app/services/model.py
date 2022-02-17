from abc import ABC, abstractmethod
from typing import Any


class BaseMLModel(ABC):
    @abstractmethod
    def predict(self, req: Any) -> Any:
        raise NotImplementedError


class MLModel(BaseMLModel):
    """Sample ML model"""

    def __init__(self, model_path: str) -> None:
        self.model_path = model_path

    def predict(self, input_text: str) -> float:
        return 1.0
