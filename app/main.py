from fastapi import FastAPI

from app.api.api import api_router
from app.api.heartbeat import heartbeat_router
from app.core.config import settings
from app.core.event_handler import start_app_handler, stop_app_handler

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(heartbeat_router)
app.include_router(api_router, prefix=settings.API_V1_STR, tags=["ML API"])

app.add_event_handler("startup", start_app_handler(app, settings.MODEL_PATH))
app.add_event_handler("shutdown", stop_app_handler(app))

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
