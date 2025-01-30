from fastapi import FastAPI, APIRouter

from src.app.api.reminders.handler import get as get_all_reminders
from src.app.api.reminders.handler import post as create_reminder
from src.app.api.reminders.schemas import ReminderResponse


def setup_routes(app: FastAPI) -> None:
    """Устаовить роуты эндпоинтов."""
    api_reminders_router = APIRouter(prefix='/reminders', tags=['Reminders'])

    api_reminders_router.api_route(
        path='/',
        methods=['GET'],
        response_model=list[ReminderResponse],
    )(get_all_reminders)

    api_reminders_router.api_route(
        path='/',
        methods=['POST'],
        response_model=ReminderResponse,
    )(create_reminder)

    app.include_router(api_reminders_router)
