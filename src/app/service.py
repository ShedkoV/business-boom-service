import uvicorn
from fastapi import FastAPI

from app.api.routes import setup_routes
from app.config.config import SERVICE_PORT, SERVICE_HOST

app = FastAPI()
setup_routes(app)


if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host=SERVICE_HOST,
        port=SERVICE_PORT,
    )