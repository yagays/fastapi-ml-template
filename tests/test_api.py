from http import HTTPStatus

from fastapi.testclient import TestClient

from app.core.config import settings


def test_healthz(client: TestClient) -> None:
    r = client.get("/healthz")
    assert r.status_code == HTTPStatus.OK


def test_api_predict(client: TestClient) -> None:
    r = client.post(f"{settings.API_V1_STR}/predict", json={"input_text": "test"})
    assert r.status_code == HTTPStatus.OK
    assert "result" in r.json()


def test_api_predict_invalid_input(client: TestClient) -> None:
    r = client.post(f"{settings.API_V1_STR}/predict", json={})
    assert r.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    r = client.post(f"{settings.API_V1_STR}/predict", json={"input": "test"})
    assert r.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
