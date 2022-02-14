from typing import Callable

from fastapi import FastAPI

from app.services.model import MLModel


def _startup_model(app: FastAPI, model_path: str) -> None:
    model_instance = MLModel(model_path)
    app.state.model = model_instance


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None


def start_app_handler(app: FastAPI, model_path: str) -> Callable:
    def startup() -> None:
        _startup_model(app, model_path)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        _shutdown_model(app)

    return shutdown
