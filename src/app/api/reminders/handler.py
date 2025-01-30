import app
from src.app.api.reminders.schemas import ReminderRequest, ReminderResponse


async def post(
    request: ReminderRequest,
) -> ReminderResponse:
    return ReminderResponse(
        id=1,
        user_phone="1212121",
        reminder_text="1212121",
    )


async def get() -> list[ReminderResponse]:
    return ...
