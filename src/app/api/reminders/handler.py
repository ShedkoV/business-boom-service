from typing import Annotated

from fastapi import Depends

from app.services.reminders import RemindersService
from src.app.api.reminders.schemas import ReminderRequest, ReminderResponse

service_dependency = Depends(RemindersService)


async def post(
    request: ReminderRequest,
    service: RemindersService = service_dependency,
) -> ReminderResponse:
    return await service.create_reminder(request)


async def get(
    service: Annotated[RemindersService, Depends()],
) -> list[ReminderResponse]:
    return await service.get_reminders()
